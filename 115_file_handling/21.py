import json
import os

FILENAME = "books.json"

def load_books():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_books(books):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=2)

def add_book(books):
    book = {
        "book_id": input("Book ID: "),
        "title": input("Title: "),
        "author": input("Author: "),
        "available": True
    }
    books.append(book)
    save_books(books)
    print("Book added.")

def search_book(books):
    book_id = input("Enter book ID: ")
    for book in books:
        if book["book_id"] == book_id:
            print(book)
            return
    print("Book not found.")

def issue_book(books):
    book_id = input("Enter book ID to issue: ")
    for book in books:
        if book["book_id"] == book_id:
            if book["available"]:
                book["available"] = False
                save_books(books)
                print("Book issued.")
            else:
                print("Book is already issued.")
            return
    print("Book not found.")

def return_book(books):
    book_id = input("Enter book ID to return: ")
    for book in books:
        if book["book_id"] == book_id:
            book["available"] = True
            save_books(books)
            print("Book returned.")
            return
    print("Book not found.")

def display_available(books):
    for book in books:
        if book["available"]:
            print(book)

books = load_books()
while True:
    print("\\n1 Add  2 Search  3 Issue  4 Return  5 Display available  6 Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_book(books)
    elif choice == "2":
        search_book(books)
    elif choice == "3":
        issue_book(books)
    elif choice == "4":
        return_book(books)
    elif choice == "5":
        display_available(books)
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
