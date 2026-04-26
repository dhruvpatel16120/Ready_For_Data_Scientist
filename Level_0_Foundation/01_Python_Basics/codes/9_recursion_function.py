# def recursive_function(parameters):
#     if base_case_condition:
#         return base_result
#     else:
#         return recursive_function(modified_parameters)

def fact(n):
    if n == 0:
        return 1, 0
    res, step = fact(n - 1)
    current_res = n * res
    print(f"Step {step + 1}: {n} * {res} = {current_res}")
    return current_res, step + 1

print("result and step :", fact(6))

def fact_iterative(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print("result using iterative method:", fact_iterative(6))

def fibonacci(n,step=0):
    if n == 0 or n== 1:
        return n
    else:
        print(f"fibonacci({n-1}) + fibonacci({n-2})",step)
        step += 1
        return fibonacci(n-1,step) + fibonacci(n-2,step)
print("fibonacci :",fibonacci(4))

def print_n(n):
    if n == 0:
        return 0
    else:
        print(n)
        return print_n(n-1)
print_n(1)