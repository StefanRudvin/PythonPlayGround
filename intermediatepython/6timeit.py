# Time it runs the snippet of code as many times as you want.

# Syntax:
# timeit.timeit('''code''', number=500)
# Remember! The ''code'' section needs all the stuff
# it cannot fetch variables, methods from outside the timeit function.


import timeit

# # Timeit times how long things take to make.
# print(timeit.timeit('1+3', number=50000000))
#
# input_list = range(100)
#
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
# # Generator
# xyz = (i for i in input_list if div_by_five(i))
#
# # List comprehension
# xyz = [i for i in input_list if div_by_five(i)]

print("Time for generator:", timeit.timeit('''

input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator
xyz = (i for i in input_list if div_by_five(i))

for i in xyz:
    x = i

''', number=5000))

print("Time for list comprehension:", timeit.timeit('''

input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# List comprehension
xyz = [i for i in input_list if div_by_five(i)]

for i in xyz:
    x = i

''', number=5000))


