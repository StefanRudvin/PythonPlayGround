[i for i in range(5)]  #  List comprehension
(i for i in range(5))  # Generator

# Once list is in memory, list comprehension is faster than generator. However, building list takes time and memory.

# Build your own generator. They do not return things, they yield things.


def simple_gen():
    yield 'oh'
    yield 'hello'
    yield 'there'

[print(i) for i in simple_gen()]

# A generator can be better than a for loop or list comprehension

CORRECT_COMBO = (3, 7, 4)

# To find this combo, we use for loops. Add break and found_combo to break once combo is found.

found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print("Found the combo: {0}".format((c1, c2, c3)))
                found_combo = True
                break
            print(c1, c2, c3)

# Use a generator instead! The generator produces a 'stream' that can be stopped anytime


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print("Found the combo: {0}".format((c1, c2, c3)))
        break

# 10 lines vs 12 lines +  only one break statement.
