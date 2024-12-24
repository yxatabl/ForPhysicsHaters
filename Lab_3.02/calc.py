import matplotlib.pyplot as plt
import numpy as np

U = np.array([0.04, 2.05, 2.99, 3.71, 4.40, 4.84, 5.25, 5.59, 5.90, 6.04, 6.49, 6.68, 6.89, 7.06, 7.75])
I = np.array([15.11, 12.15, 10.16, 9.69, 8.67, 8.02, 7.41, 6.92, 6.43, 6.18, 5.59, 5.30, 4.99, 4.75, 4.60])
eds = 10.45

Pr = U*I
P = eds*I

nu = Pr/P

plt.plot(I, nu, linestyle='--', color='red')
plt.plot(I, nu, 'o')
plt.xlabel("I, мА")
plt.ylabel("nu")
plt.grid()
plt.savefig("graph.png")