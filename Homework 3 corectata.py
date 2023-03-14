

def your_function_1 (a, b, c, d, e):
   return  a + b +  c

result_1 = your_function_1(1, 5, -3, "abc", [12,56,"cad"])
print ( result_1)

def your_function_2(*args):
    return 0
result_2 = your_function_2()
print (result_2)

def your_function_3 (a, b, c,*args, **e ):
    return a + b
result_3 = your_function_3(2, 4, "abc", param_1=2)
print (result_3)



def my_function_sum(n):
    if n == 0:
        return 0
    else:
        return (n + my_function_sum(n-1))
result_sum_function = my_function_sum(65)
print(result_sum_function)



def my_function_even(n):#
    if n == 0:
        return 0
    elif n % 2 == 1:
        return my_function_even(n-1)
    else:
        return n + my_function_even(n-2)
result_even_sum_function = my_function_even(7)
print (result_even_sum_function)


def my_function_odd(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return my_function_odd(n-1)
    else:
        return n + my_function_odd(n-1)
result_odd_sum_function = my_function_odd(5)
print(result_odd_sum_function)

def my_function_special():
    try:
        value = int(input("Here enter an number:"))
        return value
    except ValueError:
        return 0
my_function_special()
