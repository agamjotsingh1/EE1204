import matplotlib.pyplot as plt
import numpy as np
from utils import vecfield

epsilon_not = 8.85418e-12
k = 1/(4*np.pi*epsilon_not)
threshold = 2

def E_Q(X, Y, q, pos):
    Rx = X - pos[0]
    Ry = Y - pos[1]
    norm = np.sqrt(Rx**2 + Ry**2)
    #norm[norm < threshold] = threshold
    return k*q*(X - pos[0])/norm**3, k*q*(Y - pos[1])/norm**3

def E(X, Y):
    E1 = E_Q(X, Y, 1, (0, 1))
    E2 = E_Q(X, Y, 1, (0, -1))
    E3 = E_Q(X, Y, -1, (1, 0))
    E4 = E_Q(X, Y, -1, (-1, 0))
    return E1[0] + E2[0] + E3[0] + E4[0], E1[1] + E2[1] + E3[1] + E4[1]

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

U, V = E(X, Y)

magnitude = np.sqrt(U**2 + V**2)
U_norm = U / magnitude
V_norm = V / magnitude

plt.figure(figsize=(6, 6))
quiver_plot = plt.quiver(X, Y, U_norm, V_norm, magnitude, cmap='gnuplot')

'''
# Sample data: (x, y) coordinates and labels
points = [(1, 0, '1C'), (0, -1, '1C'), (1, 0, '-1C'), (-1, 0, '-1C')]

# Extract x, y coordinates and labels
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]
labels = [p[2] for p in points]

# Create scatter plot
plt.scatter(x_vals, y_vals, color='black', marker='.')

# Annotate each point with its label
for x, y, label in points:
    plt.text(x, y, label, fontsize=8, ha='right', va='bottom', color='black')
'''

plt.colorbar(quiver_plot, label='Electric Field Magnitude')
plt.show()
