# Q30. Store patient names and ages using lists. Add, Delete, Search, Display, Count.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

patient_names = ["Prithvi", "Rahul", "Sneha"]
patient_ages = [22, 35, 28]

while True:
    print("\n--- Patient Management Menu ---")
    print("1. Add a Patient")
    print("2. Delete a Patient")
    print("3. Search a Patient")
    print("4. Display All Patients")
    print("5. Count Total Patients")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        patient_names.append(name)
        patient_ages.append(age)
        print(name, "added.")
    elif choice == 2:
        name = input("Enter patient name to delete: ")
        if name in patient_names:
            index = patient_names.index(name)
            patient_names.pop(index)
            patient_ages.pop(index)
            print(name, "deleted.")
        else:
            print(name, "not found.")
    elif choice == 3:
        name = input("Enter patient name to search: ")
        if name in patient_names:
            index = patient_names.index(name)
            print("Patient Found -> Name:", name, "| Age:", patient_ages[index])
        else:
            print(name, "not found.")
    elif choice == 4:
        print("\nAll Patients:")
        for i in range(len(patient_names)):
            print("Name:", patient_names[i], "| Age:", patient_ages[i])
    elif choice == 5:
        print("Total patients:", len(patient_names))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")