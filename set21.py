# Students enrolled in two courses
python_course = {"Aman", "Bhavna", "Chetan", "Divya"}
java_course = {"Chetan", "Divya", "Esha", "Farhan"}

print("Students enrolled in both courses:", python_course.intersection(java_course))
print("Students enrolled in only one course:", python_course.symmetric_difference(java_course))
