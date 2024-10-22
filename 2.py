def accept_marks(A):    
    n = int(input("Enter the total number of students: ")) 
    for i in range(n): 
        while True: 
            x = input(f"Enter marks scored in FDS for student {i+1} (or 'AB' for absent): ") 
            if x == "AB": 
                A.append(-1)  # indicates absent students
                break 
            try:
                x = int(x)
                if 0 <= x <= 30:
                    A.append(x)
                    break
                else:
                    print("Please enter valid marks between 0 and 30.")
            except ValueError:
                print("Invalid input. Please enter a number or 'AB'.")
    print("Marks accepted & stored successfully.")

def display_marks(A): 
    print("\nMarks Scored in FDS") 
    for i, mark in enumerate(A, 1): 
        print(f"\tStudent {i}: {'AB' if mark == -1 else mark}")

def find_average_score(A): 
    valid_marks = [mark for mark in A if mark != -1]
    if valid_marks:
        avg = sum(valid_marks) / len(valid_marks)
        print(f"\nAverage score of class is {avg:.2f}\n")
    else:
        print("\nNo valid scores available to calculate average.\n")

def find_highest_and_lowest_score(A): 
    valid_marks = [(mark, idx+1) for idx, mark in enumerate(A) if mark != -1]
    if valid_marks:
        max_mark, max_student = max(valid_marks)
        min_mark, min_student = min(valid_marks)
        print(f"Highest Mark: {max_mark} (Student {max_student})")
        print(f"Lowest Mark: {min_mark} (Student {min_student})")
    else:
        print("\nNo valid scores available.\n")

def count_absent_students(A): 
    absent_count = A.count(-1)
    print(f"\nAbsent Student Count = {absent_count}")

def find_most_frequent_mark(A): 
    valid_marks = [mark for mark in A if mark != -1]
    if valid_marks:
        most_frequent_mark = max(set(valid_marks), key=valid_marks.count)
        freq = valid_marks.count(most_frequent_mark)
        print(f"\nMarks with highest frequency: {most_frequent_mark} (Frequency: {freq})")
    else:
        print("\nNo valid marks available to determine frequency.\n")

def main(): 
    FDS_Marks = [] 
    options = {
        1: accept_marks,
        2: find_average_score,
        3: find_highest_and_lowest_score,
        4: count_absent_students,
        5: find_most_frequent_mark
    }
    
    while True: 
        print("\nMenu:")
        print("1: Accept FDS Marks")
        print("2: Average score of class")
        print("3: Highest and lowest scores of class")
        print("4: Count of absent students")
        print("5: Display mark with highest frequency")
        print("6: Exit")
        
        try:
            choice = int(input("Enter your choice: ")) 
            if choice == 6:
                print("End of Program")
                break
            elif choice in options:
                options[choice](FDS_Marks)
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

main()
