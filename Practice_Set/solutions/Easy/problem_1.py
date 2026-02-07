# Print a welcome message for a school management system.

from sympy.printing.tree import print_node
def Welcome_message():
    print("Welcome to the School Management System")
    print("Please login to continue")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    return choice

choice = Welcome_message()

if choice == 1: print("login page loaded")
elif choice == 2: print("register page loaded")
elif choice == 3: print("exit")
else: print("invalid choice")
