s1={1,2,3,4,5}
s2={6,7,8,9,10}
print("Set 1 :",s1)
print("Set 2 :",s2)
if s1.isdisjoint(s2):
    print("The two sets have no elements in common")
else:
    print("The two sets have elements in common")