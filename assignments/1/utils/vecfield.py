import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps

cmap = colormaps['hot'].resampled(10)

def norm_with_lim(x_lim, y_lim):
    return np.sqrt((x_lim[0] - x_lim[1])**2 + (y_lim[0] - y_lim[1])**2)

# h -> radius step size
def plot_field(field, x_lim, y_lim, h):
    x_range = np.arange(x_lim[0], x_lim[1], h)
    y_range = np.arange(y_lim[0], y_lim[1], h)
    ref = (x_lim[0] + x_lim[1])/2 + (y_lim[0] + y_lim[1])/2
    norm_lim = norm_with_lim(x_lim, y_lim)

    for x1 in x_range:
        for y1 in y_range:
            x, y = field(x1, y1)
            norm = norm_with_lim((x1, 0), (y1, y_lim[0]))
            plt.quiver(x1, y1, x, y, width=0.003, headwidth=4, color=cmap(norm/norm_lim))
