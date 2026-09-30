# Q17. Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

student1_subjects = {"Python", "Maths", "Physics", "English"}
student2_subjects = {"Python", "Chemistry", "Maths", "Biology"}

common_subjects = student1_subjects & student2_subjects

print("Student 1 Subjects:", student1_subjects)
print("Student 2 Subjects:", student2_subjects)
print("Subjects studied by BOTH students:", common_subjects)