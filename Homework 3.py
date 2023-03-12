
#Homework 3:

#  Exercise 1.a)
#def your_function (a, b, c, d, e):
#   return  a + b +  c

#result = your_function(1, 5, -3, "abc", [12,56,"cad"])
#print ( result)


# Exercise 1.b)
#def your_function(*args):
#    return 0
#result = your_function()
#print (result)



# Exercise 1.c)

#def your_function (a, b, c,*args, **e ):
#    return a + b
#result = your_function(2, 4, "abc", param_1=2)
#print (result)


# Exercise 2.a)

#def my_function(n):
#    if n == 0:
#        return 0
#    else:
#        return (n + my_function(n-1))
#result = my_function(65)
#print(result)


# Exercitiul 2.b)
#def my_function(n):
#    if n == 0:
#        return 0
#    elif n % 2 == 1:
#        return my_function(n-1)
#    else:
#        return n + my_function(n-2)
#result = my_function(7)         
#print (result)


# Exercitiul 2.c)
#def my_function(n):
#    if n == 0:
#        return 0
#    elif n % 2 == 0:
#        return my_function(n-1)
#    else:
#        return n + my_function(n-1)
#result = my_function(5)
#print(result)



# Exercitiul 3.
#def my_function():
#    try:
#        value = int(input("Here enter an number:"))
#        return value
#    except ValueError:
#        return 0
#my_function()
