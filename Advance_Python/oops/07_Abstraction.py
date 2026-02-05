# 🎓 Lesson 07: Abstraction
# 🏛️ Topic: Abstract Base Classes (ABC)

from abc import ABC, abstractmethod

"""
ABSTRACTION: Hiding the complexity and showing only the dashboard.
Abstract Class: A class that cannot be instantiated. It acts as a set of rules.
Abstract Method: A method that has a declaration but no body. Subclasses MUST implement it.
"""

class PaymentMethod(ABC): # Inheriting from ABC turns this into an Abstract Class
    
    @abstractmethod
    def process_payment(self, amount):
        """Rule: Any payment method must define how to process payment."""
        pass

    def transaction_report(self):
        """Abstract classes can have regular methods too!"""
        print("Finalizing standard transaction report...")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"💰 Processing ${amount} via PayPal API...")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"💳 Swiping card for ${amount} via SecureGateway...")

# --- EXECUTION ---

# Attempting to create an object of abstract class (WILL FAIL)
# p = PaymentMethod() # TypeError: Can't instantiate abstract class PaymentMethod

p1 = PayPal()
p1.process_payment(500)
p1.transaction_report()

p2 = CreditCard()
p2.process_payment(200)

# 🔍 Why use this?
# It enforces a "Contract". If you add a 'Bitcoin' class, 
# you HAVE to implement 'process_payment', or your code won't run.
