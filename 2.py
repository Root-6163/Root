# Function to accept marks
def accept_marks(marks):
    n = int(input("Enter the total number of students: "))
    for i in range(n):
        while True:
            score = input(f"Enter the marks for student {i + 1} (or AB for absent): ")
            if score == "AB":
                marks.append(-1)  # Use -1 for absent students
                break
            try:
                score = int(score)
                if 0 <= score <= 30:
                    marks.append(score)
                    break
                else:
                    print("Please enter valid marks (0-30).")
            except ValueError:
                print("Invalid input. Try again.")
    print("Marks accepted and stored successfully.")

# Function to display marks
def display_marks(marks):
    print("\nMarks Scored in FDS:")
    for i, mark in enumerate(marks):
        if mark == -1:
            print(f"\tStudent {i + 1}: AB")
        else:
            print(f"\tStudent {i + 1}: {mark}")

# Function to calculate average score
def find_average_score(marks):
    valid_marks = [mark for mark in marks if mark != -1]
    if valid_marks:
        avg = sum(valid_marks) / len(valid_marks)
        print(f"\nAverage score of class: {avg:.2f}")
    else:
        print("\nNo valid marks to calculate average.")

# Function to find highest and lowest scores
def find_highest_and_lowest(marks):
    valid_marks = [mark for mark in marks if mark != -1]
    if valid_marks:
        highest = max(valid_marks)
        lowest = min(valid_marks)
        print(f"\nHighest score: {highest}")
        print(f"Lowest score: {lowest}")
    else:
        print("\nNo valid marks to find highest or lowest.")

# Function to count absent students
def count_absent_students(marks):
    absent_count = marks.count(-1)
    print(f"\nNumber of absent students: {absent_count}")

# Function to find the mark with the highest frequency
def mark_with_highest_frequency(marks):
    valid_marks = [mark for mark in marks if mark != -1]
    if valid_marks:
        most_frequent = max(set(valid_marks), key=valid_marks.count)
        freq = valid_marks.count(most_frequent)
        print(f"\nMark with highest frequency: {most_frequent} ({freq} times)")
    else:
        print("\nNo valid marks to find frequency.")

# Main function with menu
def main():
    marks = []
    while True:
        print("\n1: Accept Marks")
        print("2: Average Score of Class")
        print("3: Highest and Lowest Scores")
        print("4: Count of Absent Students")
        print("5: Mark with Highest Frequency")
        print("6: Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            accept_marks(marks)
            display_marks(marks)
        elif choice == '2':
            find_average_score(marks)
        elif choice == '3':
            find_highest_and_lowest(marks)
        elif choice == '4':
            count_absent_students(marks)
        elif choice == '5':
            mark_with_highest_frequency(marks)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

main()
