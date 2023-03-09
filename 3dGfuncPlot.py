import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from math import e

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(-4, 3, 0.25)
Y = np.arange(-3, 4, 0.25)
X, Y = np.meshgrid(X, Y)
Z = (2-e**(-X**2-Y**2)-0.5*e**(-(X+1.5)**2-(Y-2)**2))
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(1, 3)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()