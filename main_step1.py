# main.py
# Step 1 Demo: Basics of Python with Multiple Students (CO1, CO2, CO3, CO4)

# OUTPUT
print("Hello! This is your Personal Expense Tracker (Step 1, Multiple Students).")

# MULTIPLE STUDENTS using list of dictionaries (CO1, CO3)
students = [
    {"name": "Tahzib", "age": 20, "balance": 2000.75, "is_student": True},
    {"name": "Tanvi", "age": 19, "balance": 5000.50, "is_student": True}
]

# FUNCTION (CO2)
def greet(user):
    """Function to greet user"""
    print("Hi,", user)

# STRING OPERATIONS (CO4) — only once
greeting = "welcome to python"
print(greeting.upper())        # Convert to uppercase
print(greeting.capitalize())   # Capitalize first letter
print("-" * 30)

# LOOP through each student (CO2 - control structure)
for student in students:
    print("Your name is " + student["name"])  # Concatenation
    print(f"Your balance is Rs.{student['balance']}")  # f-string
    
    # DATA STRUCTURES (CO3)
    items = ["pen", "notebook"]                # List
    record = ("01-10-2025", "Food", 100.0)     # Tuple
    info = {"name": student["name"], "balance": student["balance"]}  # Dictionary
    unique_cats = {"Food", "Travel"}           # Set

    # ARITHMETIC OPERATION (CO1)
    new_balance = student["balance"] + 500
    print("Updated balance:", new_balance)

    # CALL FUNCTION
    greet(student["name"])

    print("-" * 30)  # separator between students
print("Thank you for using the Personal Expense Tracker!")