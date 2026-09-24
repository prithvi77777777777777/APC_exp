"""4.	Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers."""
import numpy as np
arr = np.arange(1, 21)
odd=arr[arr %2 !=0]
even=arr[arr%2==0]
print("Array: ", arr)
print("Odd Numbers: ", odd)
print("Even Numbers: ", even)