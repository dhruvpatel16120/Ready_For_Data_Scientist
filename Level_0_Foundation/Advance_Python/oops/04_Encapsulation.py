# 🎓 Lesson 04: Encapsulation
# 🏛️ Topic: Public, Protected, and Private Attributes

"""
PYTHON NAMING CONVENTIONS:
- name: Public (Accessible everywhere)
- _name: Protected (Internal use, accessible but discouraged outside sub-classes)
- __name: Private (Name mangled, very hard to access directly outside class)
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._account_type = "Savings" # Protected
        self.__balance = balance    # Private (Hidden and Secure)

    # 🛡️ Using Getter (Accessor)
    def get_balance(self):
        return self.__balance

    # 🛡️ Using Setter (Mutator)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def __secret_process(self): # Private Method
        print("Running internal security check...")

# --- EXECUTION ---

acc = BankAccount("Dhruv", 1000)

# 1. Accessing Public
print(f"Owner: {acc.owner}")

# 2. Accessing Protected (Possible, but shows warning in IDEs)
print(f"Type: {acc._account_type}")

# 3. Accessing Private (THROWS ERROR)
# print(acc.__balance) # Raises AttributeError

# 4. Correct way to interact with private data
print(f"Balance via Getter: {acc.get_balance()}")
acc.deposit(500)

# 5. Name Mangling (Technical way Python hides private attributes)
# You CAN access it via _ClassName__AttributeName (BUT DON'T DO IT!)
print(f"Mangled Access: {acc._BankAccount__balance}")
