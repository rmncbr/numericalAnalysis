# this program solves a system of equations by using Gaussian Elimination.
import sys

def gaussianElimination():
    # basic info about the matrix
    A = [[-2, -4, 6, 1, -6, 4, 1, -6, 47],                   # defining a 2 dimensional array of doubles
         [-4, -10, 16, 3, -10, 4, 4, -6, 88],                # change as desired
         [4, 4, -6, -1, 10, -12, 1, 18, -85],
         [2, 6, -6, 1, 12, -4, -2, 10, -76],
         [4, 4, 2, 2, 36, -26, 5, 50, -199],
         [4, 10, -14, -4, 18, 0, -7, 32, -173],
         [-6, -10, 12, 0, -26, 30, 3, -20, 111],
         [-6, -6, 8, -1, -14, 30, 9, -18, 45]]

    rows = len(A)                                           # number of rows of A
    cols = len(A[0])                                        # number of columns of A
                                                            #   - the number of elements in the first row
    print("matrix")
    for i in range(0, rows):
        print(A[i])

    # triangularize
    for c in range(0, cols-2):                                  # get zeros below pivot column by column
        for r in range(c+1, rows):                              # for each column, add to rows below. note that c+1 is variable, not constant
                                                                # could add pivoting here to get a non-zero pivot if A[c][c]==0
            multiple = (A[r][c])/(A[c][c])                      # multiple to get zeros below pivot
            for k in range(0, cols):                            # going down each column in row r
                A[r][k] = (A[r][k]) - (multiple * (A[c][k]))    # add multiple of pivot row c to row r

    # print the triangularized matrix
    print("\ntriangularized matrix")
    for i in range(0, rows):
        print(A[i])

    # back-substitution
    x = [0, 0, 0, 0, 0, 0, 0, 0]                            # 1 dimensional array of individual variable solutions
    x[rows-1] = (A[rows-1][cols-1])/(A[rows-1][cols-2])
    for r in range(rows-2, -1, -1):                         # decrementing up from 2nd to last equation to 0th equation
        x[r] = A[r][cols-1]                                 # solution r starts with constant term
        for c in range(r+1, cols-1):                        # subtract all the variable terms to the right
            x[r] = x[r] - ((A[r][c]) * x[c])                # of the pivot column (r+1 is variable)
        x[r] = x[r]/(A[r][r])                               # divide by coefficient of the pivot variable

    # print the solution
    print("\nsolution")
    print(x)

if __name__ == '__main__':                                  # run it up!!!
    sys.exit(gaussianElimination())


