#!/usr/bin/env python

import numpy as np
from matplotlib.pyplot import colorbar, show, subplots

results = np.loadtxt("data.dat")

fig, ax = subplots()
image = ax.imshow(results, vmin=-3, vmax=3, extent=(-1, 1, -1, 1))

show()
