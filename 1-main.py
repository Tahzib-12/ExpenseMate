# 1-main.py
# Personal Expense Tracker - Step 3
# Group Mini Project
# Submitted By: Tahzib Pathan, Tanvi Katrujwar
# College: G.H. Raisoni College of Engineering and Management, Pune

import os

# -------------------------------
# CO3: Using data structures (list of dictionaries) to store multiple student info
# -------------------------------
students = [
    {"name": "Tahzib", "age": 20, "balance": 2000.75},
    {"name": "Tanvi", "age": 19, "balance": 5000.50}
]

# CO4: File handling for storing expenses
expense_file = "expenses.txt"

LOW_BALANCE_THRESHOLD = 500  # Low balance warning threshold

# -------------------------------
# Function to greet users (CO1: basic input/output, CO2: function usage)
# -------------------------------
def greet(user):
    print("Hi,", user)

greeting = "welcome to the ExpenseMate"
print(greeting.upper())   # CO4: string method used (uppercase)
print(greeting.capitalize())
print("-" * 30)

# -------------------------------
# Add Expense (CO1, CO2, CO3, CO4)
# -------------------------------
def add_expense():
    student_name = input("Enter student name: ")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))

    # CO4: Save expense to file
    with open(expense_file, "a") as file:
        file.write(f"{student_name},{date},{category},{amount}\n")

    # CO3: Update balance automatically
    for student in students:
        if student['name'].lower() == student_name.lower():
            student['balance'] -= amount
            print(f"Updated balance for {student['name']}: Rs.{student['balance']}")
            # Low balance warning
            if student['balance'] < LOW_BALANCE_THRESHOLD:
                print("⚠️ Warning: Low balance!")
            break
    print("Expense added successfully.\n")

# -------------------------------
# View Expenses (CO2, CO4, CO1)
# -------------------------------
def view_expenses():
    if os.path.exists(expense_file):
        print("\n--- All Expenses ---")
        with open(expense_file, "r") as file:
            for line in file:
                name, date, category, amount = line.strip().split(",")
                print(f"{date} | {name} | {category} | Rs.{amount}")
        print("-------------------\n")
    else:
        print("No expenses found.\n")

# -------------------------------
# Search Expenses (CO2, CO4)
# -------------------------------
def search_expenses():
    search_name = input("Enter student name to search: ")
    found = False
    if os.path.exists(expense_file):
        with open(expense_file, "r") as file:
            for line in file:
                name, date, category, amount = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"{date} | {name} | {category} | Rs.{amount}")
                    found = True
    if not found:
        print("No expenses found for this student.\n")

# -------------------------------
# Summary Expenses (CO2, CO3, CO4)
# -------------------------------
def summary_expenses():
    totals = {}
    if os.path.exists(expense_file):
        with open(expense_file, "r") as file:
            for line in file:
                name, date, category, amount = line.strip().split(",")
                amount = float(amount)
                if name in totals:
                    totals[name] += amount
                else:
                    totals[name] = amount
        print("\n--- Total Expenses per Student ---")
        for name, total in totals.items():
            print(f"{name}: Rs.{total}")
        print("-------------------\n")
    else:
        print("No expenses found.\n")

# -------------------------------
# Delete Expense (CO2, CO3, CO4)
# -------------------------------
def delete_expense():
    del_name = input("Enter student name for deleting expense: ")
    del_date = input("Enter date of expense (DD-MM-YYYY): ")
    updated_data = []
    found = False
    deleted_amount = 0
    if os.path.exists(expense_file):
        with open(expense_file, "r") as file:
            for line in file:
                name, date, category, amount = line.strip().split(",")
                if name == del_name and date == del_date:
                    found = True
                    deleted_amount = float(amount)
                    continue
                updated_data.append(line)
        with open(expense_file, "w") as file:
            file.writelines(updated_data)

        if found:
            # CO3: Restore balance after deleting expense
            for student in students:
                if student['name'].lower() == del_name.lower():
                    student['balance'] += deleted_amount
                    print(f"Updated balance for {student['name']}: Rs.{student['balance']}")
                    break
            print("Expense deleted successfully.\n")
        else:
            print("No matching expense found.\n")
    else:
        print("No expenses file found.\n")

# -------------------------------
# View Balances (CO3)
# -------------------------------
def view_balances():
    print("\n--- Current Balances ---")
    for student in students:
        balance = student['balance']
        print(f"{student['name']}: Rs.{balance}")
        if balance < LOW_BALANCE_THRESHOLD:
            print("⚠️ Warning: Low balance!")
    print("------------------------\n")

# -------------------------------
# Main Menu (CO1, CO2)
# -------------------------------
while True:
    print("Personal Expense Tracker - Step 3")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Summary (Total per Student)")
    print("5. Delete Expense")
    print("6. View Balances")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expenses()
    elif choice == "4":
        summary_expenses()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        view_balances()
    elif choice == "7":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")

print("Thank you for using the ExpenseMate!")
