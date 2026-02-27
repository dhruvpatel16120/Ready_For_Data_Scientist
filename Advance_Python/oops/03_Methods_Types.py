# 🎓 Lesson 03: Types of Methods
# 🏛️ Topic: Instance, Class, and Static Methods

class Pizza:
    _pizza_type = "Margherita"
    pizza_price = 200
    pizza_ingredients = ["mozzarella", "tomatoes"]

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    # 1. INSTANCE METHOD
    # Used to access or modify the object state (instance variables).
    # Needs 'self' as a parameter.
    def description(self):
        print(f"Pizza Type: {self._pizza_type}") # it will print class variable
        return f"A {self.size} inch pizza with {', '.join(self.toppings)}."

    # 2. CLASS METHOD
    # Used to access or modify the class state (class variables).
    # Uses @classmethod decorator and 'cls' as a parameter.
    @classmethod
    def change_pizza_type(cls):
        cls._pizza_type = "Cheese" # Modifying class variable
        return cls(12, ["mozzarella", "tomatoes"]) # Factory Method

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
print(my_pizza._pizza_type)
my_pizza._pizza_type = "onion" # prote
print(f"My Pizza: {my_pizza.description()}")

# Create using Class Method (Factory Method)
chef_special = Pizza.change_pizza_type()
print(f"Chef's Special: {chef_special.description()}")

# Using Static Method (No object needed)
topping = "Spinach"
print(f"Is {topping} healthy? {Pizza.is_healthy(topping)}")
