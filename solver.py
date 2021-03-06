#!/usr/bin/env python3
from sympy import solve, symbols, Eq, cos
import math

data = [
    {
        'a': 21.8,
        'b': 50.8
    },
    {
        'a': 48.5,
        'b': 2.3
    }
]

while True:
    x, y = symbols('x y', nonnegative=True)
    equations = []

    for i in [0,1]:
        try:
            theta_str = input('Input {}{}(deg):'.format(u"\u03F4", i+1))
            cos_theta = cos(math.radians(float(theta_str)))
            print('cos(theta)=' + str(round(cos_theta, 6)))
        except Exception as e:
            print("Error reading theta value, input was: " + theta_str)
            print(e)
            exit(-1)
        except KeyboardInterrupt:
            print('')
            print('Ctrl-C detected, exiting')
            exit(0)
            
        a = data[i]['a']
        b = data[i]['b']
        A = (a+b) * (cos_theta + 1)
        equation = Eq(A, 4*( a*x/(a+x) + b*y/(b+y)))
        equations.append(equation)

    try:
        sol = solve(equations, [x,y])
        x, y = sol[0]
    except Exception as e:
        print('Error solving the equation, something is wrong')
        print(e)

    print('Result: {} {}'.format(x, y))