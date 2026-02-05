# loop statement 

# while loop statement with infinite loop
while True:
    print("infinite loop")
    break

# while loop statement with condition
a = 10
while a > 0:
    print("value of a :", a)
    a = a - 1
print("while loop ended !..")

# for loop statement with range
for i in range(5):
    print("value of i in for loop :", i)
print("for loop ended !..")

# for loop statement with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("fruit name :", fruit)
print("for loop with list ended !..")

# nested for loop statement
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)
print("nested for loop ended !..")

# for loop with else statement
for i in range(3):
    print("value of i in for loop with else :", i)
else:
    print("for loop with else ended !..")

# while loop with else statement
b = 3

while b > 0:
    print("value of b in while loop with else :", b)
    b = b - 1
else:
    print("while loop with else ended !..")

# break statement in for loop
for i in range(10):
   if i == 5:
      break
print("value of i before break :", i) 

# continue statement in for loop
for i in range(10):
    if i % 2 == 0:
        continue
    print("odd value of i using continue :", i)

# pass statement in for loop
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print("value of i using pass :", i)