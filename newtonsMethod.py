# this program finds the root of a differentiable function f(x) via Newton's Method
# a separate function sqrt(x) is included utilizing Newton's Method to find square roots

import sys
def newtonsMethod():
    oldEst = 1                          # initial guess
    tol = 0.5 * (10 ** -8)              # tolerance - change for desired tolerance
    n = 0                               # number of iterations
    nmax = 50                           # max number of iterations - limit
    while True:                         # do-while loop
        newEst = f(oldEst)              # recurrence relation - create new estimate x_i+1
        err = abs(newEst - oldEst)      # absolute error stopping criterion
        oldEst = newEst                 # we don't need to keep the old estimates
        n = n + 1                       # running total of iterations
        if err < tol or n == nmax:      # if our absolute error is less than the tolerance, or we have reached our iteration limit, break
            break
    print(str(newEst))

def f(x):
    print("x:" + str(x))
    return (2*(x ** 3) +1)/(3*(x ** 2) + 1)  # the function to test, change as desired

def sqrt(x):
    return (x + (5/x))/2                # aka the babylonian method,
                                        # used to find square roots: (radicand/x) -> (x + (a/x))/2
                                        # returns square root of 5


if __name__ == '__main__':              # run it up!!!
    sys.exit(newtonsMethod())


