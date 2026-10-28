import numpy as np

arr = np.array([12, 55, 32, 78, 49, 91, 50, 63, 25, 100])
arr[arr > 50] = 0
print("Updated array:", arr)
