tutor = False

def pancakesort(data):
    if len(data) <= 1:
        return data
    if tutor: print()
    for size in range(len(data), 1, -1):
        maxindex = max(range(size), key=data.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                data[:maxindex+1] = reversed(data[:maxindex+1])
            # Flip it into its final position
            data[:size] = reversed(data[:size])
    if tutor: print()

if __name__ == '__main__':
    import random

    myrange = max(range(5))
    print("Should be 4:", myrange)

    tutor = True
    data = list('45321')
    #while data == sorted(data):
        #random.shuffle(data)
    print('Original List: %r' % ' '.join(data))
    pancakesort(data)
    #data = reversed(data)
    print('Pancake Sorted List: %r' % ' '.join(data))
