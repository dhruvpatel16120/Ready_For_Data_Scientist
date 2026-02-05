# File: demo_subpackages.py
# This script demonstrates how to import from sub-packages.

# Method 1: Importing specific modules from sub-packages
from ecommerce.payments import stripe
from ecommerce.products import inventory

print("--- Sub-package Demonstration ---")

# Using product sub-package
product = inventory.get_product_details(101)
print(f"Product Info: {product}")

# Using payment sub-package
if product != "Product not found":
    stripe.process_payment(product['price'])

print("\n--- Another way to import ---")
# Method 2: Importing specific functions
from ecommerce.payments.stripe import process_payment

process_payment(500)
