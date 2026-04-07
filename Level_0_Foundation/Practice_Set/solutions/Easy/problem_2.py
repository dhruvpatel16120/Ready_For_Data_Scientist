# Print your name, age, and city on separate lines.

def print_data(name,age,city):
    print(f"\nmy name is {name}.\n I am {age} years old.\n I live in {city}.")

name = input("Enter your name :")
age = int(input("Enter Your Age: "))
city = input("Enter your City Name:")

print_data(name,age,city)
