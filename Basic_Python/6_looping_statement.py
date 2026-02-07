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
   if i == 5: # 1> 0 , 2> 1, 3> 2, 4> 3, 5> 4, 6> 5
      break
print("value of i before break :", i) 

# continue statement in for loop
for i in range(10):
    if i % 2 == 0: # 0%2==0 True, 1%2==0 False, 2%2==0 True, 3%2==0 False, 4%2==0 True, 5%2==0 False, 6%2==0 True, 7%2==0 False, 8%2==0 True, 9%2==0 False, 10%2==0 True
        continue # 0,2,4,6,8,10 are skipped and loop continues
    print("odd value of i using continue :", i)

# pass statement in for loop
for i in range(5):
    if i == 3: 
        pass  # Placeholder for future code
    print("value of i using pass :", i)

# for loop with dictionary
dict = {"name": "Dhruv", "age": 21, "city": "Ahmedabad"}
for key, value in dict.items():
    print(f"{key} : {value}")
print("for loop with dictionary ended !..")

# print in table format
print("\n")
print("|","key","value","|")
print("|","-----","-----","|")
for key, value in dict.items():
    print(f"|{key:5}|{value:5}|")
print("|","-----","-----","|")

# print dict keys only
for key in dict.keys():
    print(key)
print("for loop with dictionary keys ended !..")

# print dict values only
for value in dict.values():
    print(value)
print("for loop with dictionary values ended !..")

value = ""
count = 0

while value:
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue
print("while loop ended !..")