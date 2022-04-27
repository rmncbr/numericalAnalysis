# this program finds the root of a continuous function via the bisection method.
# f(x) is the function to be tested.

import sys

def bisection():
    a = 2                       # left endpoint
    b = 3                       # right endpoint
    tol = 0.5 * (10 ** -8)      # test tolerance - a root is correct to within p decimal places
                                #   if the solution is less than tol
    fa = f(a)                   # f(a)
    fb = f(b)                   # f(b)

    while True:                 # do-while loop
        c = (a + b) / 2         # midpoint
        fc = f(c)               # f(c) - f(midpoint)
        if fc == 0:             # if the midpoint is the exact root, break
            break
        if (fa * fc) < 0:       # if f(c) is the opposite sign of f(a),
            b = c               # assign c as the new right endpoint
            fb = fc
        else:                   # else, make c the new left endpoint
            a = c
            fa = fc
        if (b - a) / 2 < tol:   # stop if the interval length/2 is within tolerance
            break

    c = (a + b) / 2             # calculate the final root estimate
    print(str(c))


def f(x):
    return (x ** 2) - 5         # function to test, change as desired

if __name__ == '__main__':      # run it up !!!
    sys.exit(bisection())

