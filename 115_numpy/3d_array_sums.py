import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)
print("Array:\\n", arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer (axis=0):\\n", np.sum(arr, axis=0))
print("Sum along rows (axis=2):\\n", np.sum(arr, axis=2))
print("Sum along columns (axis=1):\\n", np.sum(arr, axis=1))
