# Q22. Create two sets representing technical skills of two employees. Find common skills, unique skills, and all available skills.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

emp1_skills = {"Python", "SQL", "Java", "HTML"}
emp2_skills = {"Java", "JavaScript", "SQL", "CSS"}

print("Employee 1 Skills:", emp1_skills)
print("Employee 2 Skills:", emp2_skills)
print("Common Skills:", emp1_skills & emp2_skills)
print("Skills unique to Employee 1:", emp1_skills - emp2_skills)
print("Skills unique to Employee 2:", emp2_skills - emp1_skills)
print("All Available Skills:", emp1_skills | emp2_skills)