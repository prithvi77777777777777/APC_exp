import student

name = input("Student name: ")
marks = [float(input(f"Marks in subject {i + 1}: ")) for i in range(5)]
total = student.total_marks(marks)
percentage = student.percentage(marks)
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", student.grade(percentage))
