'''
4 Problem 4 : Multiple Subplots Matplotlib1 30 https://www.geeksforgeeks.org/how-to-create-multiple-subplots-in-matplotlib-in-python/
'''

# importing library
import matplotlib.pyplot as plt # type: ignore

# Some data to display
x = [1, 2, 3]
y = [0, 1, 0]
z = [1, 0, 1]

# Creating 2 subplots
fig, ax = plt.subplots(2)

# Accessing each axes object to plot the data through returned array
ax[0].plot(x, y)
ax[1].plot(x, z)

# importing library
import matplotlib.pyplot as plt # type: ignore
import numpy as np

# Data for plotting
x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)

# Creating 6 subplots and unpacking the output array immediately
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
ax1.plot(x, y, color="orange")
ax2.plot(x, y, color="green")
ax3.plot(x, y, color="blue")
ax4.plot(x, y, color="magenta")
ax5.plot(x, y, color="black")
ax6.plot(x, y, color="red")

import matplotlib.pyplot as plt # type: ignore

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Now axs is a 2D array of Axes objects
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 1].scatter([1, 2, 3], [4, 5, 6])
axs[1, 0].bar([1, 2, 3], [4, 5, 6])
axs[1, 1].hist([1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5])

plt.show()

