import curses
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.nodelay(1)
stdscr.timeout(100)

# Set up the game window
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.border()

# Set up the Tetromino shapes
tetrominos = [
    [['.', 'O', '.'],
     ['O', 'O', 'O'],
     ['.', '.', '.']],
     
    [['I', 'I', 'I', 'I'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']],
     
    [['.', 'Z', 'Z'],
     ['Z', 'Z', '.'],
     ['.', '.', '.']],
     
    [['T', 'T', 'T'],
     ['.', 'T', '.'],
     ['.', '.', '.']],
     
    [['L', '.', '.'],
     ['L', 'L', 'L'],
     ['.', '.', '.']],
     
    [['.', '.', 'J'],
     ['J', 'J', 'J'],
     ['.', '.', '.']],
     
    [['.', '.', '.'],
     ['.', 'S', 'S'],
     ['S', 'S', '.']]
]

# Set up the game variables
score = 0
lines = 0
speed = 0.1
current_piece = None
current_x = sw // 2 - 2
current_y = 0

# Function to draw a Tetromino piece on the game window
def draw_piece(piece, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] != '.':
                w.addch(y + row, x + col, piece[row][col])

# Function to check for collision with walls or other pieces
def is_collision(piece, x, y):
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if piece[row][col] != '.' and (w.inch(y + row, x + col) != ord(' ')):
                return True
    return False

# Function to rotate a Tetromino piece
def rotate_piece(piece):
    return list(zip(*reversed(piece)))

# Function to clear completed rows
def clear_rows():
    global score, lines, speed
    rows_cleared = 0
    for row in range(sh - 2, 0, -1):
        if '.' not in [chr(w.inch(row, col)) for col in range(1, sw - 1)]:
            w.addstr(row, 1, ' ' * (sw - 2))
            for r in range(row, 1, -1):
                w.addstr(r, 1, ''.join([chr(w.inch(r - 1, col)) for col in range(1, sw - 1)]))
            rows_cleared += 1
    score += 10 * rows_cleared
    lines += rows_cleared
    speed = 0.1 + (lines // 10) * 0.02

# Function to reset the game variables
def reset_game():
    global score, lines, speed, current_piece, current_x, current_y
    score = 0
    lines = 0
    speed = 0.1
    current_piece = None
    current_x = sw // 2 - 2
    current_y = 0

# Main game loop
while True:
    # Create a new piece if there is none
    if current_piece is None:
        current_piece = random.choice(tetrominos)
        current_x = sw // 2 - 2
        current_y = 0
        if is_collision(current_piece, current_x, current_y):
            reset_game()

    # Handle user input
    key = w.getch()
    if key == ord('q'):
        break
    elif key == curses.KEY_LEFT:
        if not is_collision(current_piece, current_x - 1, current_y):
            current_x -= 1
    elif key == curses.KEY_RIGHT:
        if not is_collision(current_piece, current_x + 1, current_y):
            current_x += 1
    elif key == curses.KEY_DOWN:
        if not is_collision(current_piece, current_x, current_y + 1):
            current_y += 1
    elif key == ord('r'):
        rotated_piece = rotate_piece(current_piece)
        if not is_collision(rotated_piece, current_x, current_y):
            current_piece = rotated_piece

    # Move the current piece down
    if not is_collision(current_piece, current_x, current_y + 1):
        current_y += 1
    else:
        # Merge the current piece with the game grid
        for row in range(len(current_piece)):
            for col in range(len(current_piece[row])):
                if current_piece[row][col] != '.':
                    w.addch(current_y + row, current_x + col, current_piece[row][col])
        clear_rows()
        current_piece = None

    # Draw the game window
    w.clear()
    w.border()
    w.addstr(0, sw // 2 - 4, ' Tetris ')
    w.addstr(2, sw // 2 - 6, f' Score: {score} ')
    w.addstr(3, sw // 2 - 6, f' Lines: {lines} ')
    w.addstr(sh - 1, sw // 2 - 10, ' Press "Q" to quit ')
    draw_piece(current_piece, current_x, current_y)
    w.refresh()

    # Speed up the falling of pieces
    curses.napms(int(speed * 1000))

# Clean up the screen
curses.endwin()
print(f"Game Over! Score: {score} Lines: {lines}")





# chatgpt copied didnt feel like the motivation of continuing