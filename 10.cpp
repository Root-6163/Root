#include <iostream>
#include <cstring> // For strlen and strcmp
#define MAX 20

using namespace std;

class Stack {
private:
    int top, topeval;               // Indices for the stack and evaluation stack
    char infix[MAX], postfix[MAX];  // Infix and postfix expressions
    char stk[MAX];                  // Stack for characters
    float stkeval[MAX];             // Evaluation stack for float values

public:
    Stack();                        // Constructor
    void push(char temp);           // Push character onto the stack
    void pusheval(float temp);      // Push float onto the evaluation stack
    void read();                    // Read infix expression
    int isEmpty();                  // Check if character stack is empty
    int isEmptyeval();              // Check if evaluation stack is empty
    char pop();                     // Pop character from the stack
    float popeval();                // Pop float from the evaluation stack
    void convert_infix_postfix();   // Convert infix to postfix
    int priority(char x);           // Get priority of operators
    float evaluatePostfix();        // Evaluate the postfix expression
};

// Constructor
Stack::Stack() {
    top = -1;       // Initialize top of character stack
    topeval = -1;   // Initialize top of evaluation stack
}

// Check if the character stack is empty
int Stack::isEmpty() {
    return (top == -1) ? -1 : 1; // Return -1 if empty, otherwise return 1
}

// Check if the evaluation stack is empty
int Stack::isEmptyeval() {
    return (topeval == -1) ? -1 : 1; // Return -1 if empty, otherwise return 1
}

// Push a character onto the stack
void Stack::push(char temp) {
    if (top < MAX - 1) { // Check for stack overflow
        stk[++top] = temp; // Increment top and add character
    } else {
        cout << "Stack is Full\n";
    }
}

// Push a float onto the evaluation stack
void Stack::pusheval(float temp) {
    if (topeval < MAX - 1) { // Check for stack overflow
        stkeval[++topeval] = temp; // Increment topeval and add float
    } else {
        cout << "Evaluation Stack is Full\n";
    }
}

// Pop a character from the stack
char Stack::pop() {
    if (isEmpty() == -1) {
        cout << "Stack is Empty\n";
        return '@'; // Return a placeholder for empty stack
    }
    return stk[top--]; // Return the top element and decrement top
}

// Pop a float from the evaluation stack
float Stack::popeval() {
    if (isEmptyeval() == -1) {
        cout << "Evaluation Stack is Empty\n";
        return -999; // Return a placeholder for empty evaluation stack
    }
    return stkeval[topeval--]; // Return the top float and decrement topeval
}

// Read the infix expression
void Stack::read() {
    cout << "Enter infix expression: ";
    cin >> infix;
}

// Convert infix expression to postfix
void Stack::convert_infix_postfix() {
    char sop;
    int k = 0; // Index for postfix expression

    for (int i = 0; infix[i] != '\0'; i++) {
        if (isdigit(infix[i])) {
            postfix[k++] = infix[i]; // Add digits to postfix
        } else if (infix[i] == '(') {
            push(infix[i]); // Push '(' onto stack
        } else if (infix[i] == ')') {
            while ((sop = pop()) != '(') { // Pop until '('
                postfix[k++] = sop;
            }
        } else { // Operator
            while (priority(infix[i]) <= priority(sop = pop())) {
                if (top == -1) break; // Break if stack is empty
                postfix[k++] = sop;
            }
            if (priority(infix[i]) > priority(sop)) {
                push(sop); // Re-push operator for comparison
            }
            push(infix[i]); // Push the current operator
        }
    }

    while (top != -1) { // Pop remaining operators
        postfix[k++] = pop();
    }
    postfix[k] = '\0'; // Null-terminate the postfix string
    cout << "The postfix expression is: " << postfix << endl;
}

// Return the priority of operators
int Stack::priority(char x) {
    switch (x) {
        case '(': return 0;
        case '+':
        case '-': return 1;
        case '*':
        case '/': return 2;
        default: return -1; // Invalid operator
    }
}

// Evaluate the postfix expression
float Stack::evaluatePostfix() {
    float value, operand1, operand2, result;

    for (int i = 0; postfix[i] != '\0'; i++) {
        if (isdigit(postfix[i])) {
            value = postfix[i] - '0'; // Convert char to float
            pusheval(value);
        } else { // Operator
            operand2 = popeval();
            operand1 = popeval();
            switch (postfix[i]) {
                case '+': result = operand1 + operand2; break;
                case '-': result = operand1 - operand2; break;
                case '*': result = operand1 * operand2; break;
                case '/': result = operand1 / operand2; break;
                default: result = 0; break; // Handle invalid operators
            }
            pusheval(result);
        }
    }
    return popeval(); // Return the final result
}

int main() {
    Stack s;           // Create a stack object
    s.read();          // Read infix expression
    s.convert_infix_postfix(); // Convert infix to postfix
    float answer = s.evaluatePostfix(); // Evaluate the postfix expression
    cout << "The answer is: " << answer << endl; // Output the result
    return 0;
}
