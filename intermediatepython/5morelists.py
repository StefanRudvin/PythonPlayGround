input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

# xyz = []
# for i in input_list:
#    if div_by_five(i):
#        xyz.append(i)

# for i in xyz:
#    print(i)

# [print(i) for i in xyz]

xyz = [i for i in input_list if div_by_five(i)]

#print(xyz)

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
# print(primes)

# One liner for loops use list comprehension enclosed in []
# () is for generators, and behave differently, ie. cannot call print()

# [print(i) for i in xyz]


# The two methods below are identical. One line for loop.

# [[print(i, ii) for ii in range(5)] for i in range(5)]

# for i in range(5):
#    for ii in range(5):
#        print(i, ii)

# List comprehension
xyz = [[[i, ii] for ii in range(5)] for i in range(5)]
print(xyz)

# Generator expression
xyz = ([[i, ii] for ii in range(5)] for i in range(5))
print([i for i in xyz])


xyz = (((i, ii) for ii in range(5)) for i in range(5))

for i in xyz:
    for ii in i:
        # print(ii)
        pass

# This is possible (but takes time)
# xyz = (((i, ii) for ii in range(900000000000)) for i in range(900000000000))

# This is not possible due to ram limitations
# xyz = [[(i, ii) for ii in range(900000000000)] for i in range(900000000000)]

xyz = (print(i) for i in range(5))

for i in xyz:
    i  # This works because i already includes the print statement.




