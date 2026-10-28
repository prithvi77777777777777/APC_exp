from library_app.books.catalog import list_books
from library_app.members.records import list_members
from library_app.transactions.records import list_transactions

print("Books:", list_books())
print("Members:", list_members())
print("Transactions:", list_transactions())
