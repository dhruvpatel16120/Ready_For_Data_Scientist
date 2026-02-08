"""
05: Custom Exceptions
=====================

You can create your own exception classes by inheriting from the built-in 
'Exception' class. This is best practice for large applications where 
Standard exceptions (like ValueError) aren't descriptive enough.

syntax:
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
"""

# 1. Define custom exception class
class InsufficientFundsError(Exception):
    """Exception raised when account balance is less than withdrawal."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Withdrawal of {amount} failed. Current Balance: {balance}"
        super().__init__(self.message)

# 2. Use the custom exception
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

print("--- [05] Custom Exception Demo ---")

account_balance = 900
withdrawal_amount = 250

try:
    while account_balance > 0:
        print(f"Balance: {account_balance}, Attempting withdraw: {withdrawal_amount}")
        new_balance = withdraw(account_balance, withdrawal_amount)
        print(f"Remaining Balance: {new_balance}")
        account_balance = new_balance

except InsufficientFundsError as e:
    print(f"❌ Transaction Alert: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
