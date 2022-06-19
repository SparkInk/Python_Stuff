import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting import plot
import numpy as np
x = Symbol('x');

eqnOriginal = x**3 - 2 * x**2 - 11 * x + 12; # f(x)
eqnDiff = eqnOriginal.diff(); # f'(x)

plt.grid(True)

for discreteInterval in np.arange(-6, 6, 0.001):

    mainYAxis = eqnOriginal.subs(x, discreteInterval)
    
    root = discreteInterval
    
    if round(eqnDiff.subs(x, root)) == 0:
       blackPlot = plt.plot(discreteInterval, 0, 'k.');
       plt.plot(discreteInterval, mainYAxis, 'm.');
       continue;
    else:
        newRoot = root - eqnOriginal.subs(x, root) / eqnDiff.subs(x, root);
        while abs(root - newRoot) > 0.1:
          root = newRoot;
          newRoot = root - eqnOriginal.subs(x, root) / eqnDiff.subs(x, root);


    if round(newRoot) == -3:
     plt.plot(discreteInterval, 0, 'r.');
     plt.plot(discreteInterval, mainYAxis,'m.');
    elif round(newRoot) == 1:
     plt.plot(discreteInterval, 0, 'b.');
     plt.plot(discreteInterval, mainYAxis,'m.');
    elif round(newRoot) == 4:
     plt.plot(discreteInterval, 0, 'g.');
     plt.plot(discreteInterval, mainYAxis,'m.');

plt.figure(figsize=(20,20))
plt.show()
