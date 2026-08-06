'''5.	Create a list of student names. Remove:
•	First student 
•	Last student 
•	A specific student by name 
'''

st=['Prithvi','harsh','prathmesh','atharv','anmol']
print(st)
st.remove('anmol')
print(st)
ls=len(st)-1
st.remove(st[ls])
print("After removing lasy student:",st)
s=input("Enter name to remove:\t")
st.remove(s)
print("After removing specific student:",st)
