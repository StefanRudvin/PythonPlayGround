# The zip function is used to 'join' lists, even with different data types.

x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a, b, c in zip(x, y, z):
    print(a, b, c)

# print(zip(x, y, z)) # Zip object

# a zip is essentially a list of tuples.
for i in zip(x, y, z):
    print(i)

# Use the list() function to convert the object into a list.
# print(list(zip(x, y, z)))

# Use the dict() function to convert the object into a dictionary. However, only uses 2 values.
# print(dict(zip(x, y)))

[print(a, b, c) for a, b, c in zip(x, y, z)]

# String concatenation does not save the looping values, but real for loops do!
# However, this can be good since using the loop variable (x) can overwrite previous variables!

[print(a, b) for a, b in zip(x, y)]
# print(a) # not found!

for x, y in zip(x, y):
    print(x, y)

print(x)  # Found!







