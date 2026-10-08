str=input("Enter string")
count=0
char=""
l=[]
d=set()

for i in str:
	if i not in d:
		d.add(i)
	l.append(i)
	
for j in d:
	temp=l.count(j)
	if count< temp:
		count=temp
		char=j
print("Character:", char ,"\tCount:", count)

