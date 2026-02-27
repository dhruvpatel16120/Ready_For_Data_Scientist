# 🎓 Lesson 02: Constructors, Attributes, and Methods
# ===================================================

class Smartphone:
    # 🌍 1. CLASS ATTRIBUTES (Shared by all instances)
    category = "Electronics"
    platform = "Mobile"

    # 🛠️ 2. CONSTRUCTORS (__init__)
    
    # In Python, you can only have ONE __init__ method. 
    # To handle "Multiple Constructors", we use default arguments.
    
    def __init__(self, brand="Generic", price=0, ram="4GB"):
        """
        This single method acts as:
        1. Default/Non-parameterized (if called without args)
        2. Parameterized (if called with args)
        """
        # 🆔 3. INSTANCE ATTRIBUTES (Unique to each object)
        self.brand = brand
        self.price = price
        self.ram = ram
        print(f"--- Log: Device Created ({self.brand}) ---")

    # 🏃 4. TYPES OF METHODS

    # A. INSTANCE METHOD: Needs 'self'. Can access instance and class variables.
    def show_details(self):
        print(f"Brand: {self.brand} | Price: {self.price} | RAM: {self.ram}")
        print(f"Category: {self.category}") # Accessing class attribute

    # B. CLASS METHOD: Needs '@classmethod' and 'cls'. 
    # Used to modify class state or create factory methods.
    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform
        print(f"All devices updated to platform: {cls.platform}")

    # C. STATIC METHOD: Needs '@staticmethod'. No 'self' or 'cls'.
    # Pure utility function related to the class but doesn't touch its data.
    @staticmethod
    def check_5g_support(area_code):
        if area_code > 500:
            return "5G Supported"
        return "4G Only"

# ==========================================
# 🚀 DEMONSTRATION
# ==========================================

# 1. Using Non-parameterized Constructor (uses defaults)
phone1 = Smartphone()
phone1.show_details()

# 2. Using Parameterized Constructor
phone2 = Smartphone("Samsung", 50000, "8GB")
phone2.show_details()

# 3. Accessing Attributes
print(f"\nPhone 1 Brand: {phone1.brand}") # Instance
print(f"Common Category: {Smartphone.category}") # Class

# 4. Calling Class Methods
# Affects the CLASS, not just one object.
Smartphone.change_platform("Smart Device")
print(f"Phone 2 Platform: {phone2.platform}")

# 5. Calling Static Methods
# Called using Class Name (or instance, but Class name is better)
result = Smartphone.check_5g_support(650)
print(f"Network Status: {result}")

class Student:
    def __init__(self):
        self.__name = "Jethalal"
        self.age = "40"
        self.gender = "Male"
        self.city = "Mumbai"
        self.occupation = "Owner of Gada Electronics"

    def show_details(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"City: {self.city}")
        print(f"Occupation: {self.occupation}")

student1 = Student()
student1.name = "Karan"
student1.show_details()

# 💡 SUMMARY TABLE:
# -------------------------------------------------------------
# Type           | Accesses         | Decorator      | Param
# -------------------------------------------------------------
# Instance Method| self (Object)    | None           | self
# Class Method   | cls (Class)      | @classmethod   | cls
# Static Method  | None             | @staticmethod  | None
# -------------------------------------------------------------
