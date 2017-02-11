array = list(5,4,3,2,1)
for size in range(len(array), 1, -1):
    print("Current size:", size)
    maxindex = max(range(size), key=array.__getitem__)
    print("maxindex:", maxindex)
