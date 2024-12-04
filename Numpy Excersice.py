# import numpy as np

# n = 1000
# steps = np.random.choice([-1, 1], size=n)
# walk = np.cumsum(steps)

# import matplotlib.pyplot as plt
# plt.plot(walk)
# plt.show()

import matplotlib.pyplot as plt

fig, axs = plt.subplots()

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')

axs[0, 1].bar(x, y)
axs[0, 1].set_title('Bar Plot')

axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Scatter Plot')

axs[1, 1].pie(y, labels=x)
axs[1, 1].set_title('Pie Chart')

plt.tight_layout()
plt.show()

