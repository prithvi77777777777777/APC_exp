"""8.	Create a 3 × 4 matrix and display its transpose."""
import numpy as np
a1=np.arange(1,13).reshape(3,4)
print("original :",a1,"\n\n")
print("transpose matrix:\n\n",np.transpose(a1))