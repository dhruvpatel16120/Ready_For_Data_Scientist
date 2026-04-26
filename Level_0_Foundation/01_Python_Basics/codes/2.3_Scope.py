# scope of variables 

a = 10 # global variable

def example_function():
    b = 20 # local variable
    print("Local variable:", b)
    print("Global variable:", a)

example_function()
print("Global variable:", a)
# print("Local variable:", b) # it will give error because local variable is not accessible outside the function

## example of global and nonlocal variables and nonlocal keyword
global_var = 10

def example_function():
    local_var = 20
    global global_var # use global keyword for variables in the global (module) scope
    global_var = 20
    def inner():
        nonlocal local_var # use nonlocal keyword for variables in the enclosing function scope
        local_var = 30
        print("Local variable:", local_var)
        print("Global variable:", global_var)
    inner()

example_function()
# print("local variable outside the function:", local_var) # it will give error because local variable is not accessible outside the function
print("Global variable outside the function:", global_var)
# print("nonlocal variable outside the function:", nonlocal global_var) # it will give error because nonlocal variable is not accessible outside the function 