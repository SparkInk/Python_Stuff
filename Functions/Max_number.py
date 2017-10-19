#Finds out a maximum number of a sequence
#Also it lets you choose a way of writing
#P.S. it's for python3
import random
L = list()
m = input('A way to fill sequence: 1 -> random or 2 -> by yourself?\n')
if m == '1':
    n = int(input('Enter a number up to random seq:\n'))
    max = 0
    for i in range(0, n):
        L.append(random.randint(0, n ** 2))
    for i in range(0, len(L)):
        if L[i] > max:
            max = L[i]
    print('The sequence is', L)
    print('Max number in seq is ', max)
elif m == '2':
    n = int(input('How many numbers you are going to enter?\n'))
    for i in range(0, n):
        L.append(int(input('Enter number:\n ')))
    max = 0
    for i in range(0, len(L)):
        if L[i] > max:
            max = L[i]
    print('The sequence is', L)
    print('Max number in seq is', max)
else: 
    print('Wrong number. Please try again')

 
