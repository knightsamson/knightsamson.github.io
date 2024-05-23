#define the functions needed, add, sub, mul, div
# print options to the user
#ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))



def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("input your choices: ")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number:  "))
    b = int(input("input second number:  "))
    add(a, b)
elif choice == "b" or choice == "B":
    print("Substraction")
    a = int(input("input first number:  "))
    b = int(input("input second number:  "))
    sub(a, b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number:  "))
    b = int(input("input second number:  "))
    mul(a, b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("input first number:  "))
    b = int(input("input second number:  "))
    div(a, b)
elif choice == "e" or choice == "E":
    print("Program ended")
    quit()