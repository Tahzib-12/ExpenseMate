# main.py
# Step 2 Demo: File Handling + Expense Records (CO1-CO4)

import os

# MULTIPLE STUDENTS
students = [
    {"name": "Alice", "age": 20, "balance": 1500.75},
    {"name": "Bob", "age": 21, "balance": 2000.50}
]

# FILE NAME
expense_file = "expenses.txt"

# FUNCTION TO ADD EXPENSE
def add_expense():
    student_name = input("Enter student name: ")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    
    # Save as CSV line: name,date,category,amount
    with open(expense_file, "a") as file:
        file.write(f"{student_name},{date},{category},{amount}\n")
    print("Expense added successfully.\n")

# FUNCTION TO VIEW ALL EXPENSES
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

# MAIN MENU
while True:
    print("Personal Expense Tracker - Step 2")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again.\n")
print("Thank you for using the Personal Expense Tracker!")