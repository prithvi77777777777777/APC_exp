import csv

filename = "attendance.csv"

try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))

    for row in records:
        total = int(row["Total_Classes"])
        attended = int(row["Classes_Attended"])
        percentage = attended / total * 100 if total else 0
        row["Attendance_Percentage"] = percentage

    print("Students with attendance below 75%:")
    for row in records:
        if row["Attendance_Percentage"] < 75:
            print(row["Name"], "-", round(row["Attendance_Percentage"], 2), "%")
except FileNotFoundError:
    print("attendance.csv not found.")
