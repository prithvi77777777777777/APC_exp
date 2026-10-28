import csv

filename = "transactions.csv"

try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        transactions = list(csv.DictReader(file))

    deposits = [float(row["Amount"]) for row in transactions if row["Type"].lower() == "deposit"]
    withdrawals = [float(row["Amount"]) for row in transactions if row["Type"].lower() == "withdrawal"]

    total_deposits = sum(deposits)
    total_withdrawals = sum(withdrawals)
    balance = total_deposits - total_withdrawals
    largest = max(transactions, key=lambda row: float(row["Amount"])) if transactions else None

    print("Total deposits: ₹", total_deposits)
    print("Total withdrawals: ₹", total_withdrawals)
    print("Final balance: ₹", balance)
    print("Largest transaction:", largest)
except FileNotFoundError:
    print("transactions.csv not found.")
