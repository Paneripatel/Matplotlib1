'''
2 Problem 2 : Pyplot in Matplotplib ( https://www.geeksforgeeks.org/python-introduction-matplotlib/ )
'''

import matplotlib.pyplot as plt # type: ignore

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt # type: ignore

x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]

fig, ax = plt.subplots()  
ax.plot(x, y, marker='o', label="Data Points")

ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis") 
ax.set_ylabel("Y-Axis")  


plt.show()