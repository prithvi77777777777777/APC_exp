#Write a PYTHON program to evaluate the student performance
 #     If % is >=90 then Excellent
 # If % is >=70 then Good performance
 #  If % is >=60 then average performance
 # else Poor performance.

m1=int(input("Enter marks for subject 1:"))
m2=int(input("Enter marks for subject 2:")) 
m3=int(input("Enter marks for subject 3:")) 
m4=int(input("Enter marks for subject 4:"))

total=m1+m2+m3+m4
per=(total/400)*100
print("percentage =",per)
if per>=90 and per<100:
    print("Excellent performance ")
elif per>=70 and per<=89:
    print("Good performance")
elif per>=60 and per<=69:
    print("Average performance")
else:
    print("poor performance")
