def get_the_sum(*args,**kwargs):
    total = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            total += arg
        elif type(arg) == list or type(arg) == tuple:
            total += get_the_sum(*arg)
    for arg in kwargs.values():
        if type(arg) == int or type(arg) == float:
             total += arg
        elif type(arg) == list or type(arg) == set:
            total += get_the_sum(**kwarg)
    return total
print(get_the_sum(1, 5, -3, "abc", "12", [12, 56, "cad"]))
print(get_the_sum(1, 5, -3, "abc", "12", [12, 56, [1, 2], "cad"]))
print(get_the_sum(1, 5, -3, "abc", "12", [12, 56, [1, 2, {3, 4}], "cad"]))
print(get_the_sum(2, 4, "abc", param_1=2))
print(get_the_sum(2, 4, "abc", param_1=2, param_2="abc"))
print(get_the_sum(2, 4, "abc", param_1=2, param_2="abc", param_3=2.5))
