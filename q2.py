"""2.	Create two NumPy arrays of 5 integers each. Perform and display:
•	Addition 
•	Subtraction 
•	Multiplication 
•	Division 
•	Modulus
"""

import numpy as np
ar1=np.array([1,2,3,4,5])
ar2=np.array([10,9,8,7,6])
print("Array 1:", ar1)
print("Array 2:", ar2)
print("Addition:\n", ar1 + ar2)
print("Subtraction:\n", ar1 - ar2)
print("Multiplication:\n", ar1 * ar2)
print("Division:\n", ar1 / ar2)
print("Modulus:\n", ar1 % ar2)