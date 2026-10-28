import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
flat = arr.flatten()
print("Original array:\\n", arr)
print("Flattened array:", flat)
