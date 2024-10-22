def accept_matrix():
    print("\nEnter the order of the Matrix (row, col): ")
    r = int(input("\trow = "))
    c = int(input("\tcol = "))
    matrix = []
    print("Enter the elements of the Matrix:")
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"Element [{i+1},{j+1}]: ")))
        matrix.append(row)
    print("\nMatrix accepted successfully\n")
    return matrix, r, c

def display_matrix(M, r, c):
    print(f"\nMatrix ({r},{c}):")
    for i in range(r):
        print("\t", end=' ')
        for j in range(c):
            print(f"{M[i][j]:3d}", end=' ')
        print("")

def addition_matrix(M1, M2, r, c):
    return [[M1[i][j] + M2[i][j] for j in range(c)] for i in range(r)]

def subtraction_matrix(M1, M2, r, c):
    return [[M1[i][j] - M2[i][j] for j in range(c)] for i in range(r)]

def multiplication_matrix(M1, M2, r1, c1, c2):
    M3 = []
    for i in range(r1):
        row = []
        for j in range(c2):
            sum = 0
            for k in range(c1):
                sum += M1[i][k] * M2[k][j]
            row.append(sum)
        M3.append(row)
    return M3

def transpose_matrix(M, r, c):
    return [[M[j][i] for j in range(r)] for i in range(c)]

def main():
    M1, M2, r1, c1, r2, c2 = [], [], 0, 0, 0, 0

    while True:
        print("\n1: Accept Matrix")
        print("2: Display Matrix")
        print("3: Addition of Matrices")
        print("4: Subtraction of Matrices")
        print("5: Multiplication of Matrices")
        print("6: Transpose Matrix")
        print("7: Exit")

        ch = int(input("Enter your choice: "))

        if ch == 7:
            print("End of Program")
            break

        if ch == 1:
            print("Input First Matrix")
            M1, r1, c1 = accept_matrix()
            print("Input Second Matrix")
            M2, r2, c2 = accept_matrix()

        elif ch == 2:
            print("\tFirst Matrix:")
            display_matrix(M1, r1, c1)
            print("\tSecond Matrix:")
            display_matrix(M2, r2, c2)

        elif ch == 3:
            if r1 == r2 and c1 == c2:
                M3 = addition_matrix(M1, M2, r1, c1)
                print("\tAddition Result:")
                display_matrix(M3, r1, c1)
            else:
                print("Addition not possible (orders are not the same)")

        elif ch == 4:
            if r1 == r2 and c1 == c2:
                M3 = subtraction_matrix(M1, M2, r1, c1)
                print("\tSubtraction Result:")
                display_matrix(M3, r1, c1)
            else:
                print("Subtraction not possible (orders are not the same)")

        elif ch == 5:
            if c1 == r2:
                M3 = multiplication_matrix(M1, M2, r1, c1, c2)
                print("\tMultiplication Result:")
                display_matrix(M3, r1, c2)
            else:
                print("Multiplication not possible (columns of 1st matrix != rows of 2nd matrix)")

        elif ch == 6:
            print("\tTranspose of First Matrix:")
            M3 = transpose_matrix(M1, r1, c1)
            display_matrix(M3, c1, r1)
            print("\tTranspose of Second Matrix:")
            M3 = transpose_matrix(M2, r2, c2)
            display_matrix(M3, c2, r2)

        else:
            print("Wrong choice entered! Try again.")

if __name__ == "__main__":
    main()
