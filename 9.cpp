#include <iostream>
#include <cstring> // For strlen and strcmp
#define MAX 50    // Define a constant for the maximum size

using namespace std;

class Stack {
private:
    char a[MAX]; // Array to hold stack elements
    int top;     // Index of the top element

public:
    Stack() { top = -1; } // Constructor to initialize top

    void push(char c);         // Push character onto stack
    void reverse();            // Reverse the string using stack
    void convert(char str[]);  // Convert string to lowercase
    void palindrome();          // Check if the string is a palindrome
};

void Stack::push(char c) {
    if (top < MAX - 1) { // Check for stack overflow
        a[++top] = c;    // Increment top and add character
        cout << endl << c << " is pushed on stack ...";
    } else {
        cout << "\nStack Overflow! Cannot push " << c << " onto stack.";
    }
}

void Stack::reverse() {
    cout << "\n\nReverse string is: ";
    for (int i = top; i >= 0; i--) {
        cout << a[i]; // Print the characters in reverse order
    }
    cout << endl;
}

void Stack::convert(char str[]) {
    int k = 0; // Index for the converted string
    int len = strlen(str); // Length of the input string

    for (int j = 0; j < len; j++) {
        // Check if the character is alphabetic
        if (isalpha(str[j])) {
            // Convert to lowercase
            str[k++] = tolower(str[j]);
        }
    }
    str[k] = '\0'; // Null-terminate the converted string
    cout << endl << "Converted String: " << str << "\n";
}

void Stack::palindrome() {
    char str[MAX];
    for (int i = top; i >= 0; i--) {
        str[top - i] = a[i]; // Fill str with characters from stack
    }
    str[top + 1] = '\0'; // Null-terminate the string

    // Compare the original string with the reversed string
    if (strcmp(str, a) == 0) {
        cout << "\n\nString is a palindrome...";
    } else {
        cout << "\n\nString is not a palindrome...";
    }
}

int main() {
    Stack stack;
    char str[MAX];

    cout << "\nEnter a string to be reversed and check if it is a palindrome: \n\n";
    cin.getline(str, MAX); // Read the input string

    stack.convert(str); // Convert string to lowercase

    // Push each character onto the stack
    for (int i = 0; str[i] != '\0'; i++) {
        stack.push(str[i]);
    }

    stack.palindrome(); // Check if the string is a palindrome
    stack.reverse();     // Print the reversed string

    return 0;
}
