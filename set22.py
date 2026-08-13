
employee1_skills = {"Python", "SQL", "Git", "Excel"}
employee2_skills = {"Python", "Java", "Git", "Docker"}

print("Common skills:", employee1_skills.intersection(employee2_skills))
print("Skills unique to Employee 1:", employee1_skills.difference(employee2_skills))
print("Skills unique to Employee 2:", employee2_skills.difference(employee1_skills))
print("All available skills:", employee1_skills.union(employee2_skills))
