def accept_array():
    A = []
    n = int(input("Enter the total number of students: "))
    for i in range(n):
        x = int(input(f"Enter the roll no of student {i+1}: "))
        A.append(x)
    print("Student information accepted successfully.\n")
    return A, n

def display_array(A, n):
    if n == 0:
        print("\nNo records in the database.")
    else:
        print("Students Array: ", end=' ')
        for i in range(n):
            print(f"{A[i]} ", end=' ')
        print("\n")

def linear_search(A, n, X):
    for i in range(n):
        if A[i] == X:
            return i  # Found, return the index
    return -1  # Not found

def sentinel_search(A, n, X):
    last = A[n-1]
    i = 0
    A[n-1] = X  # Place X (search target) at the end
    while A[i] != X:
        i += 1
    A[n-1] = last  # Restore the original last element

    if i < n-1 or A[n-1] == X:  # If found or last element is the search target
        return i
    return -1  # Not found

def main():
    A = []
    n = 0
    while True:
        print("\t1: Accept & Display Students Info")
        print("\t2: Linear Search")
        print("\t3: Sentinel Search")
        print("\t4: Exit")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 4:
            print("End of Program")
            break
        
        elif ch == 1:
            A, n = accept_array()
            display_array(A, n)
        
        elif ch == 2:
            X = int(input("Enter the roll no to be searched: "))
            result = linear_search(A, n, X)
            if result == -1:
                print("\tRoll no not found.\n")
            else:
                print(f"\tRoll no found at location {result + 1}\n")
        
        elif ch == 3:
            X = int(input("Enter the roll no to be searched: "))
            result = sentinel_search(A, n, X)
            if result == -1:
                print("\tRoll no not found.\n")
            else:
                print(f"\tRoll no found at location {result + 1}\n")
        
        else:
            print("Wrong choice entered! Try again.")

if __name__ == "__main__":
    main()
