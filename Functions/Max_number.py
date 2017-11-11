#Finds out a maximum number of a sequence
#P.S. it's for python3
def max_number(n): #How many numbers you are going to enter? (should be a list)
    max = 0
    for i in range(0, len(n)):
        if n[i] > max:
            max = n[i]
    return max
