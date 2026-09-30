# Q21. Find students enrolled in both courses and students enrolled in only one course.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

python_students = {"Prithvi", "Rahul", "Sneha", "Amit"}
java_students = {"Sneha", "Amit", "Priya", "Rohit"}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Python Students:", python_students)
print("Java Students:", java_students)
print("Students in BOTH courses:", both_courses)
print("Students in ONLY ONE course:", only_one_course)