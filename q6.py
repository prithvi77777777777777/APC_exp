"""6.	Create two 3 × 3 NumPy matrices and perform matrix addition."""
import numpy as np
arr1=np.arange(1,10).reshape(3,3)
arr2=np.arange(10,19).reshape(3,3)
print("Matrix 1:\n", arr1)
print("Matrix 2:\n", arr2)
print("Matrix 1+ Matrix 2:\n",arr1,"\n\t+\n",arr2,"=\n\n", arr1 + arr2)