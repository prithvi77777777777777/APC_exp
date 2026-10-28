import csv

filename = "student_records.csv"

try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))

    for record in records:
        record["Marks"] = float(record["Marks"])

    print("All records:")
    for record in records:
        print(record)

    if records:
        top_student = max(records, key=lambda record: record["Marks"])
        average = sum(record["Marks"] for record in records) / len(records)
        print("Highest marks:", top_student)
        print("Average marks:", average)
        print("Students scoring above 80:")
        for record in records:
            if record["Marks"] > 80:
                print(record)
except FileNotFoundError:
    print("student_records.csv not found.")
