
# This is a generator. Does not use memory. Does not make a list.
# for i in range(5):

# List comprehension is faster, but it uses memory. Can take more time to begin, but iterating is faster.

# Below are two equivalent.
xyz = []
for i in range(5):
    xyz.append(i)

zxy = [i for i in range(5)]

xyz = (i for i in range(5))
# The second is a generator object, which is used for iteration.

for i in xyz:
    print(i)




