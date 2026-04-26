
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