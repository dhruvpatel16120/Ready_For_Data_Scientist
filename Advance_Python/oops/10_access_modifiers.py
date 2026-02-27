# 10 Access Modifiers

class Student:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

class Derived(Student):
    def __init__(self):
        super().__init__()
        print(self.public_var)
        print(self._protected_var)
        print(self._Student__private_var)

Base_obj = Student()
Derived_obj = Derived()

print(Base_obj.public_var)
print(Base_obj._protected_var)
print(Base_obj._Student__private_var)