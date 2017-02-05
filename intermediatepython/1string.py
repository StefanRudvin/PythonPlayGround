import os

names = ['Jeff', 'Honey', 'James', 'Samantha']

# Two ways to concatenate strings.
# Join performs much better.
for name in names:
    # print('Hello there, ' + name)
    # print(' '.join(['Hello there,', name]))
    pass
# print(', '.join(names))

location_of_file = '.'
file_name = 'example.txt'

# print(location_of_file + file_name)

with open(os.path.join(location_of_file, file_name)) as f:
    print(f.read())

who = 'Gary'
how_many = 12

# This is wrong!
# print(who, 'bought', how_many, 'apples today.')

# Use this instead as of python 3:
# print('{} bought {} apples today.'.format(who, how_many))

# Use this for python 2:
print('{0} bought {1} apples today.'.format(who, how_many))




