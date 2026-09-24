"""9.	Create a 4 × 4 NumPy array and write a program to:
•	Display the first row 
•	Display the last column 
•	Display the diagonal elements 
•	Display the elements from the second and third rows
"""

import numpy as np

a1=np.arange(1,17).reshape(4,4)
print(a1)

print("First row:\t",a1[0])
print("Last column",a1[0,3],a1[1,3],a1[2,3],a1[3,3])
print("diagonal column",a1[0,0],a1[1,1],a1[2,2],a1[3,3])
print("Second row:\t",a1[1])
print("Third row:\t",a1[2])
