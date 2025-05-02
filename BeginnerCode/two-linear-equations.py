"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


Solves a system of two linear equations by inverting a 2x2 matrix.
See the discussion and code snippets on pp 123-125 of the text for more
concise examples of the same concepts.
"""

def determinant_2x2(A):
    """
    Calculate the determinant of a 2x2 matrix A
    """
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

def inverse_2x2(A):
    detA = determinant_2x2(A)
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    B = [ [d, -b], [-c, a] ]
    # scalar times matrix operation
    for i in range(2):
        for j in range(2):
            B[i][j] = (1.0 / detA) * B[i][j]
    return B

def inner_product(a, b):
    n = len(a)
    total = 0.0
    for i in range(n):
        total += a[i] * b[i]
    return total

def multiply_matrix_with_vector(A, b):
    rows = len(A)
    C = []
    for i in range(rows):
        C += [inner_product(A[i], b)]
    return C

A = [ [3, 7], [2, 5] ]
b = [15, 11]
A_inv = inverse_2x2(A)

print(A_inv)

solution = multiply_matrix_with_vector(A_inv, b)
print(solution)
