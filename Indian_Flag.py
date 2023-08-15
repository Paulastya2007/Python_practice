import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))

plt.fill_between([0, 6], 2, 3, color='orange')

plt.fill_between([0, 6], 1, 2, color='white')

plt.fill_between([0, 6], 0, 1, color='green')

circle = plt.Circle((3, 1.5), 0.5, color='white')
plt.gca().add_patch(circle)

for i in range(24):
    x = np.sin(np.pi * i / 12) * 0.5 + 3
    y = np.cos(np.pi * i / 12) * 0.5 + 1.5
    plt.plot([3, x], [1.5, y], color='blue')

circle = plt.Circle((3, 1.5), 0.5, color='blue', fill=False)
plt.gca().add_patch(circle)

plt.xlim(0, 6)
plt.ylim(0, 3)
plt.xticks([])
plt.yticks([])
plt.show()
