# Write a python program to perform matrix operations on an M x N matrix and solve a system of linear equations.
# Use inbuilt functions to implement the operations. Get two matrices from the user.
# The program should support the following Menus,
# 1.Matrix Addition
# 2.Matrix Subtraction
# 3.Scalar Matrix Multiplication
# 4.Elementwise Matrix Multiplication
# 5.Matrix Multiplication
# 6.Matrix Transpose
# 7.Trace of a Matrix
# 8.Solve System of Linear Equations
# 9.Determinant
# 10.Inverse
# 11.Eigen Value and Eigen Vector
# 12.Exit


# Importing modules
import numpy as np


def create_matrix(m, n):

    mat = []

    for i in range(m):
        row = []
        for j in range(n):
            variable = int(input("Enter a number : "))
            row.append(variable)
        mat.append(row)

    matrix = np.array(mat)

    return matrix


# Main function
if __name__ == "__main__":

    m = int(input("Enter the number of rows in the matrix : "))
    n = int(input("Enter the number of columns in the matrix : "))

    m1 = create_matrix(m, n)
    m2 = create_matrix(m, n)
    ch = 0

    print(f"Matrix-1 :-")
    print(m1)
    print(f"Matrix-2 :-")
    print(m2)

    while 1:

        print('''
    Enter the operation to be performed:-
    1.Matrix Addition  2.Matrix Subtraction  3.Scalar Matrix Multiplication  4.Elementwise Matrix Multiplication
    5.Matrix Multiplication  6.Matrix Transpose  7.Trace of a Matrix  8.Solve System of Linear Equations
    9.Determinant  10.Inverse  11.Eigen Value and Eigen Vector  12.Exit
                    ''')

        ch = int(input("Your Choice : "))

        if ch == 1:
            print("Matrix Sum :-")
            print(np.add(m1, m2))

        elif ch == 2:
            print("Matrix Difference :-")
            print(np.subtract(m1, m2))

        elif ch == 3:
            k = int(input("Enter a scalar : "))
            mat_num = int(input("Enter the matrix number : "))
            if mat_num == 1:
                scalar_product = k*m1
                print("Matrix Product :-")
                print(scalar_product)
            elif mat_num == 2:
                scalar_product = k*m2
                print("Matrix Product :-")
                print(scalar_product)
            else:
                print("INVALID INPUT")

        elif ch == 4:
            print("Elemental Product :-")
            print(np.multiply(m1, m2))

        elif ch == 5:
            if m != n:
                print("Not possible")
            else:
                print("Matrix Multiplication:-")
                print(np.dot(m1, m2))

        elif ch == 6:
            mat_num = int(input("Enter the matrix number : "))
            if mat_num == 1:
                print("Transpose Matrix :-")
                print(np.transpose(m1))
            elif mat_num == 2:
                print("Transpose Matrix :-")
                print(np.transpose(m2))
            else:
                print("INVALID INPUT")

        elif ch == 7:
            mat_num = int(input("Enter the matrix number : "))
            if mat_num == 1:
                print("Trace : ", np.sum(m1.diagonal()))
            elif mat_num == 2:
                print("Trace : ", np.sum(m2.diagonal()))
            else:
                print("INVALID INPUT")

        elif ch == 8:
            d = []
            for i in range(m):
                var = int(input("Enter RHS value : "))
                d.append(var)
            b = np.array(d)
            mat_num = int(input("Enter the matrix number : "))
            if mat_num == 1:
                print("x : ", np.linalg.solve(m1, b))
            elif mat_num == 2:
                print("x : ", np.linalg.solve(m2, b))
            else:
                print("INVALID INPUT")

        elif ch == 9:
            if m != n:
                print("Not possible")
            else:
                mat_num = int(input("Enter the matrix number : "))
                if mat_num == 1:
                    print("Determinant : ", np.linalg.det(m1))
                elif mat_num == 2:
                    print("Determinant : ", np.linalg.det(m2))
                else:
                    print("INVALID INPUT")

        elif ch == 10:
            if m != n:
                print("Not possible")
            else:
                mat_num = int(input("Enter the matrix number : "))
                if mat_num == 1:
                    print("Inverse :-")
                    print(np.linalg.inv(m1))
                elif mat_num == 2:
                    print("Inverse :-")
                    print(np.linalg.inv(m2))
                else:
                    print("INVALID INPUT")

        elif ch == 11:
            if m != n:
                print("Not possible")
            else:
                mat_num = int(input("Enter the matrix number : "))
                if mat_num == 1:
                    print("Eigen Values : ", np.linalg.eig(m1)[0])
                    print("Eigen Vector :-")
                    print(np.linalg.eig(m1)[1])
                elif mat_num == 2:
                    print("Eigen Values : ", np.linalg.eig(m2)[0])
                    print("Eigen Vector :-")
                    print(np.linalg.eig(m2)[1])
                else:
                    print("INVALID INPUT")

        elif ch == 12:
            break

        else:
            print("INVALID INPUT")

        print(" **************************************************** ")