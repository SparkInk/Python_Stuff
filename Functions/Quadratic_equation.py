import math
print('This progamm is for sovling the quadratic equation')
P = {'a':0, 'b':0, 'c':0}
for i in P:
    print('Enter:', i)
    P[i] = int(input())
D = P['b'] ** 2 - 4 * P['a'] * P['c']
if D > 0:
    D = round(math.sqrt(D), 3)
    x1 = float()
    x2 = float()
    x1 = (-P['b'] ** 2 + D) / (2 * P['a'])
    x2 = (-P['b'] ** 2 - D) / (2 * P['a'])
    print('The roots of equation is: ')
    print('x1 ->', round(x1, 3))
    print('x2 ->', round(x2, 3))
    print('D is', round(D, 3))
elif D == 0:  
        x = float()
        x = P['b'] ** 2 / (2 * P['a'])
        print('As Discriminant D = 0, root will be only one')
        print('x ->', round(x, 3))
        print('D is', round(D, 3))
else:
        x1 = complex()
        x2 = complex()
        Dc = D ** (1/2)
        x1 = (-P['b'] ** 2 + Dc) / (2 * P['a'])
        x2 = (-P['b'] ** 2 - Dc) / (2 * P['a'])
        print('As Discriminant D < 0, root will be complex')
        print('x1 ->', x1)
        print('x2 ->', x2)
        print('D is', Dc)
        

