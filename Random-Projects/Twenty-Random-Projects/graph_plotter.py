# https://www.youtube.com/watch?v=pdy3nh1tn6I&list=PLo3f6pvDBzw1JGMPXXVFnTDJo-rRKaCQU&index=8&t=2860s&ab_channel=freeCodeCamp.org

import matplotlib.pyplot as plt

x1 = [2, 4, 5, 1]
y1 = [2, 3, 6, 4]

plt.plot(x1, y1, label = 'line 1')

x2 = [1, 2, 3, 4]
y2 = [2, 3, 4, 5]

plt.plot(x2, y2, label = 'line 2')

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines')

plt.legend()

plt.show()
