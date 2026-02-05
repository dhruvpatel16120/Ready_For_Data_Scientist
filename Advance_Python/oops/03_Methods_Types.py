# 🎓 Lesson 03: Types of Methods
# 🏛️ Topic: Instance, Class, and Static Methods

class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    # 1. INSTANCE METHOD
    # Used to access or modify the object state (instance variables).
    # Needs 'self' as a parameter.
    def description(self):
        return f"A {self.size} inch pizza with {', '.join(self.toppings)}."

    # 2. CLASS METHOD
    # Used to access or modify the class state (class variables).
    # Uses @classmethod decorator and 'cls' as a parameter.
    @classmethod
    def margherita(cls):
        # Often used as an "Alternative Constructor" (Factory Method)
        return cls(12, ["mozzarella", "tomatoes"])

    @classmethod
    def pro_size(cls):
        return cls(18, ["various"])

    # 3. STATIC METHOD
    # Does not access instance or class variables. 
    # Just a utility function that stays inside the class namespace.
    @staticmethod
    def is_healthy(topping):
        healthy_toppings = ["broccoli", "tomatoes", "spinach"]
        return topping.lower() in healthy_toppings

# --- EXECUTION ---

# Create using constructor
my_pizza = Pizza(10, ["pepperoni", "cheese"])
print(f"My Pizza: {my_pizza.description()}")

# Create using Class Method (Factory Method)
chef_special = Pizza.margherita()
print(f"Chef's Special: {chef_special.description()}")

# Using Static Method (No object needed)
topping = "Spinach"
print(f"Is {topping} healthy? {Pizza.is_healthy(topping)}")
