#!/usr/bin/env python

import numpy as np
from matplotlib.pyplot import colorbar, show, subplots

results = np.loadtxt("data.dat")

fig, ax = subplots()
image = ax.imshow(results, vmin=-3, vmax=3, extent=(-1, 1, -1, 1))
cbar = colorbar(image, ax=ax, ticks=(-2*np.pi/3, 0, 2*np.pi/3))
cbar.set_label(r'$\arg(z_n)$')
cbar.ax.set_yticklabels((r'$-\frac{2\pi}{3}$', '0', r'$\frac{2\pi}{3}$'))
ax.set_xlabel(r'$\operatorname{Re}(z_0)$')
ax.set_ylabel(r'$\operatorname{Im}(z_0)$')

show()
