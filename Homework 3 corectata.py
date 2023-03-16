
def get_the_sum(*args,**kwargs):
    total = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            total += arg
    return total
print(get_the_sum(1, 5, -3, "abc", "12", [12, 56, "cad"]))
print(get_the_sum())
print(get_the_sum(2, 4, "abc", param_1=2))



def sum_of_numbers(n: int) -> tuple:
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = sum_of_numbers(n-1)
    total_sum += n
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n
    return total_sum, even_sum, odd_sum
total_sum, even_sum, odd_sum = sum_of_numbers(7)
print("Total SUm:", total_sum)
print("Sum of Even numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)



def my_function_special():
    try:
        value = int(input("Here enter an number:"))
        return value
    except ValueError:
        return 0
my_function_special()
