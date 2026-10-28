import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original array:\\n", arr)
arr[arr > 50] = 0
print("Updated array (values > 50 replaced with 0):\\n", arr)
