def accept_array():
    A = []
    n = int(input("Enter the total number of students: "))
    print("Input roll numbers in sorted order:")
    for i in range(n):
        x = int(input(f"Enter the roll number of student {i+1}: "))
        A.append(x)
    print("Student information accepted successfully.\n")
    return A, n

def display_array(A, n):
    if n == 0:
        print("\nNo records in the database.")
    else:
        print("Students Array:", end=' ')
        for i in range(n):
            print(f"{A[i]} ", end=' ')
        print("\n")

# Recursive Binary Search
def recursive_binary_search(A, s, l, X):
    if s <= l:
        mid = (s + l) // 2
        if A[mid] == X:
            return mid
        elif X < A[mid]:
            return recursive_binary_search(A, s, mid - 1, X)
        else:
            return recursive_binary_search(A, mid + 1, l, X)
    return -1  # Not found

# Iterative Binary Search
def iterative_binary_search(A, n, X):
    s = 0
    l = n - 1
    while s <= l:
        mid = (s + l) // 2
        if A[mid] == X:
            return mid
        elif X < A[mid]:
            l = mid - 1
        else:
            s = mid + 1
    return -1  # Not found

# Fibonacci Search
def fibonacci_search(A, n, X):
    f1 = 0
    f2 = 1
    f3 = f1 + f2

    offset = -1

    while f3 < n:
        f1 = f2
        f2 = f3
        f3 = f1 + f2

    while f3 > 1:
        i = min(offset + f1, n - 1)
        if A[i] == X:
            return i  # Found
        elif A[i] > X:
            f3 = f1
            f2 = f2 - f1
            f1 = f3 - f2
        else:
            f3 = f2
            f2 = f1
            f1 = f3 - f2
            offset = i

    if f2 == 1 and offset + 1 < n and A[offset + 1] == X:
        return offset + 1  # Found

    return -1  # Not found

def main():
    A = []
    n = 0
    while True:
        print("\t1: Accept & Display Students Info")
        print("\t2: Recursive Binary Search")
        print("\t3: Iterative Binary Search")
        print("\t4: Fibonacci Search")
        print("\t5: Exit")

        ch = int(input("Enter your choice: "))

        if ch == 5:
            print("End of Program")
            break

        elif ch == 1:
            A, n = accept_array()
            display_array(A, n)

        elif ch == 2:
            X = int(input("Enter the roll number to be searched: "))
            result = recursive_binary_search(A, 0, n - 1, X)
            if result == -1:
                print("\tRoll number not found.\n")
            else:
                print(f"\tRoll number found at location {result + 1}\n")

        elif ch == 3:
            X = int(input("Enter the roll number to be searched: "))
            result = iterative_binary_search(A, n, X)
            if result == -1:
                print("\tRoll number not found.\n")
            else:
                print(f"\tRoll number found at location {result + 1}\n")

        elif ch == 4:
            X = int(input("Enter the roll number to be searched: "))
            result = fibonacci_search(A, n, X)
            if result == -1:
                print("\tRoll number not found.\n")
            else:
                print(f"\tRoll number found at location {result + 1}\n")

        else:
            print("Wrong choice entered! Try again.")

if __name__ == "__main__":
    main()
