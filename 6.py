def quick_sort(arr):
    """Function to sort an array using Quick Sort."""
    print(f"quick_sort called with: {arr}")
    if len(arr) <= 1:
        print(f"Returning base case: {arr}")
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
        print(f"Pivot chosen: {pivot}")
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        print(f"Partitioned into left: {left}, middle: {middle}, right: {right}")
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        result = sorted_left + middle + sorted_right
        print(f"Merged result: {result}")
        return result

def display_top_scores(scores, top_n=5):
    """Function to display the top N scores from the sorted array."""
    print(f"display_top_scores called with scores: {scores}, top_n: {top_n}")
    if len(scores) < top_n:
        print("The number of scores is less than", top_n)
        top_n = len(scores)
    print(f"Top {top_n} scores:")
    for score in scores[-1:-(top_n + 1):-1]:
        print(score)

# Input: Store first-year percentages of students
percentages = []

# Allow user to input percentages
n = int(input("Enter the number of students: "))
for i in range(n):
    percentage = float(input(f"Enter percentage for student {i + 1}: "))
    percentages.append(percentage)

print(f"Initial percentages: {percentages}")

# Sort the array using Quick Sort
sorted_percentages = quick_sort(percentages)

# Display the sorted percentages
print("Sorted Percentages:")
print(sorted_percentages)

# Display the top 5 scores
display_top_scores(sorted_percentages)
