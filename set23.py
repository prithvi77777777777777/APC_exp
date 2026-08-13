# Books currently in the library and books requested by a visitor
available_books = {"Python Basics", "Data Structures", "Database Systems", "Computer Networks"}
requested_books = {"Python Basics", "Operating Systems", "Database Systems"}

print("Requested books that are available:", available_books.intersection(requested_books))
