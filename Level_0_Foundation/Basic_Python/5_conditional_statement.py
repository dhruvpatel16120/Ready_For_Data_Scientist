# conditional Statements : if , elif , else

age = 18

# if statement for only single statement
if age >= 18 : print("you can watch Type A movies !")

# if statement for multi statement
if age >= 18 :
    print("you can watch Type A movies !")
    print(age)

# if else statement
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# if-elif else statement :
if age >= 18:
    print("Eligible to vote")
elif age==17:
    print("you are eligible in next years")
else:
    print("Not eligible to vote")

# nested if statement :
if age >=18:
    if age<=65:
        print("you can vote to government")
    else:
        print("you are not able to vote after 65 years !..")
else:
    print("you are in childhood !..")