# Hubspot code test

limit = 50
ar  = [1, 3, 5]
ar2 = [2, 4, 6]

def mergeArrays(ar, ar2, limit):

    arlength = len(ar)
    ar2length = len(ar2)

    arpointer = 0
    ar2pointer = 0

    mergedAr = []

    for i in range(0, (arlength + ar2length)):

        if i == limit:
            break

        if arpointer >= arlength:
            mergedAr.append(ar2[ar2pointer])
            ar2pointer += 1
        elif ar2pointer >= ar2length:
            mergedAr.append(ar[arpointer])
            arpointer += 1
        else:
            if ar[arpointer] <= ar2[ar2pointer]:
                mergedAr.append(ar[arpointer])
                arpointer += 1
            else:
                mergedAr.append(ar2[ar2pointer])
                ar2pointer += 1

    return mergedAr

print(mergeArrays(ar2, ar, limit))


def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''

        currentString = strs[0]

        for string in strs:

            for i in range(0, len(currentString)):
                if i >= len(string):
                    currentString = currentString[:i]
                    break
                if string[i] != currentString[i]:
                    currentString = currentString[:i]
                    break

        return currentString

print(longestCommonPrefix(["aa", "a"]))
