# main.py
# Personal Expense Tracker - Step 3
# Group Mini Project
# Submitted By: Student 1 (Tahejib Pathan), Student 2 (Tanvi Katrujwar)
# College: G.H. Raisoni College of Engineering and Management, Pune

import os

# MULTIPLE STUDENTS
students = [
    {"name": "Tahzib", "age": 20, "balance": 2000.75},
    {"name": "Tanvi", "age": 19, "balance": 5000.50}
]

# FILE TO STORE EXPENSES
expense_file = "expenses.txt"

# FUNCTION TO GREET STUDENTS
def greet(user):
    print("Hi,", user)

# COMMON GREETING
greeting = "welcome to the ExpenseMate"
print(greeting.upper())
print(greeting.capitalize())
print("-" * 30)

# ADD EXPENSE
def add_expense():
    student_name = input("Enter student name: ")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    
    with open(expense_file, "a") as file:
        file.write(f"{student_name},{date},{category},{amount}\n")
    print("Expense added successfully.\n")

# VIEW ALL EXPENSES
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

# SEARCH EXPENSES BY STUDENT NAME
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

# SUMMARY: Total per student
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

# DELETE EXPENSE BY STUDENT NAME AND DATE
def delete_expense():
    del_name = input("Enter student name for deleting expense: ")
    del_date = input("Enter date of expense (DD-MM-YYYY): ")
    updated_data = []
    found = False
    if os.path.exists(expense_file):
        with open(expense_file, "r") as file:
            for line in file:
                name, date, category, amount = line.strip().split(",")
                if name == del_name and date == del_date:
                    found = True
                    continue  # skip this line to delete
                updated_data.append(line)
        with open(expense_file, "w") as file:
            file.writelines(updated_data)
        if found:
            print("Expense deleted successfully.\n")
        else:
            print("No matching expense found.\n")
    else:
        print("No expenses file found.\n")

# MAIN MENU
while True:
    print("Personal Expense Tracker - Step 3")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Summary (Total per Student)")
    print("5. Delete Expense")
    print("6. Exit")
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
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
print("Thank you for using the Personal Expense Tracker!")