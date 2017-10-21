#Finds out a maximum number of a sequence
#P.S. it's for python3
L = list()
n = int(input('How many numbers you are going to enter?\n'))
for i in range(0, n):
    L.append(int(input('Enter number:\n ')))
max = 0
for i in range(0, len(L)):
    if L[i] > max:
        max = L[i]
print('The sequence is', L)
print('Max number in seq is', max)


 
