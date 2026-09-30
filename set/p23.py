# Q23. Create a set containing available books and another set containing requested books. Determine which requested books are available.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

available_books = {"Python Basics", "Data Structures", "Operating Systems", "DBMS"}
requested_books = {"Python Basics", "DBMS", "Networking", "AI"}

available_requested = available_books & requested_books

print("Available Books:", available_books)
print("Requested Books:", requested_books)
print("Requested books that are AVAILABLE:", available_requested)