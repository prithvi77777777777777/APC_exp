# addition 
ar1=[[1,2,3],[4,5,6],[7,8,9]]
ar2=[[9,8,7],[6,5,4],[3,2,1]]
print("Addition:\n")
a=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
	for j in range(0,3):
		a[i][j]=ar1[i][j]+ar2[i][j]
for  i in a:
	print(i)
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
	for j in range(0,3):
		c[i][j]=ar1[i][j]-ar2[i][j]
print("Substraction:\n")
for i in c:
	print(i)
d=[[0,0,0],[0,0,0],[0,0,0]]

print("Multiplication:\n")
for i in range(0,3):
	for i in range(0,3):
		d[i][j]=ar1[i][j]*ar2[j][i]
for i in d:
	print(i)
