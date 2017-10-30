def maxSequence(arr):
    L = list(arr)
    Ll = list()
    if L == []:
        return 0
    else:
        max = sum(L)
        j = 2
        while len(L[0:j]) < len(L):
            for i in range(0, len(L)):
                if sum(L[0+i:j+i]) > max:
                    max = sum(L[0+i:j+i])
                    L1 = L[0+i:j+i]
            j += 1
    return max, L1
