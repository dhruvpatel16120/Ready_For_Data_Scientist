# 04_Custom_Exceptions.py
# Level: 🔴 Expert (Hero)
# Topic: Creating your own Exception Classes

"""
For large projects, you often need specific error types that don't 
exist in Python's built-in library.
"""

# 1. Define a class that inherits from 'Exception'
class InsufficientBalanceError(Exception):
    """Exception raised for errors in the withdrawal amount."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempted to withdraw ${amount} with only ${balance} in account."
        super().__init__(self.message)

# 2. Use the custom exception
def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

print("--- Custom Exception Demo (Banking) ---")

my_balance = 500
withdraw_amt = 600

try:
    print(f"Current Balance: ${my_balance}")
    print(f"Requesting Withdrawal: ${withdraw_amt}")
    new_balance = withdraw_money(my_balance, withdraw_amt)
    print(f"New Balance: ${new_balance}")

except InsufficientBalanceError as error:
    print(f"❌ Transaction Failed!")
    print(f"Log: {error}")
    # You could also access specific attributes: print(error.balance)
