#for python3
#The maximum sum subarray problem consists 
#in finding the maximum sum of a contiguous subsequence 
#in an array or list of integers
def maxSequence(arr):
    L = list(arr)
    Ll = list()
    if L == []:
        return 0
    else:
        max = sum(L)
        j = 2
        while len(L[0:j]) < len(L):
            for i in range(0, len(L)):    #finding an array L[0:j], L[1:j+1], L[2:j+2], etc.
                if sum(L[0+i:j+i]) > max: #with a maximum sum of elements
                    max = sum(L[0+i:j+i]) 
                    L1 = L[0+i:j+i]
            j += 1
    return max, L1
