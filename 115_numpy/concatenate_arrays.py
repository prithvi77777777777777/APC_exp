import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Horizontal concatenation:\\n", np.concatenate((a, b), axis=1))
print("Vertical concatenation:\\n", np.concatenate((a, b), axis=0))
