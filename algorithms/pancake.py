tutor = False

def pancakesort(data):
    if len(data) <= 1:
        return data
    for size in range(len(data), 1, -1):
        maxindex = max(range(size), key=data.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                data[:maxindex+1] = reversed(data[:maxindex+1])

            data[:size] = reversed(data[:size])



if __name__ == '__main__':
    import random

    tutor = False
    data = list('12345')

    while data == sorted(data):
        random.shuffle(data)
    print('Original List: %r' % ' '.join(data))
    pancakesort(data)
    data.reverse()
    print('Pancake Sorted List: %r' % ' '.join(data))
