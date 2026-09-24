"""5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
•	2 × 6 matrix 
•	3 × 4 matrix 
•	4 × 3 matrix
"""
import numpy as np
arr = np.arange(1, 13)
print("Original Array: ", arr)
print("Reshaped 2x6 Matrix:\n", arr.reshape(2, 6))
print("Reshaped 3x4 Matrix:\n", arr.reshape(3, 4))
print("Reshaped 4x3 Matrix:\n", arr.reshape(4, 3))