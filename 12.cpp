#include <iostream>
#define MAX 100 // Maximum size of the deque

using namespace std;

class Deque {
private:
    int arr[MAX]; // Array to store the deque
    int front;    // Front index
    int rear;     // Rear index

public:
    Deque(); // Constructor to initialize the deque
    void addItemFront(int item); // Add item at the front
    void addItemRear(int item);  // Add item at the rear
    void deleteItemFront();       // Delete item from the front
    void deleteItemRear();        // Delete item from the rear
    void display();               // Display the deque
    bool isEmpty();              // Check if the deque is empty
};

// Constructor to initialize front and rear
Deque::Deque() {
    front = -1;
    rear = -1;
}

// Add an item at the front of the deque
void Deque::addItemFront(int item) {
    if (front == 0) {
        cout << "Cannot add item at front end (Overflow)" << endl;
        return;
    }
    if (front == -1) {
        front = 0; // Initialize front on the first insertion
        rear = 0;  // Initialize rear on the first insertion
    } else {
        front--; // Move front pointer back
    }
    arr[front] = item; // Insert the item
    cout << "Inserted " << item << " at front." << endl;
}

// Add an item at the rear of the deque
void Deque::addItemRear(int item) {
    if (rear == MAX - 1) {
        cout << "Cannot add item at rear end (Overflow)" << endl;
        return;
    }
    if (front == -1) {
        front = 0; // Initialize front on the first insertion
        rear = 0;  // Initialize rear on the first insertion
    } else {
        rear++; // Move rear pointer forward
    }
    arr[rear] = item; // Insert the item
    cout << "Inserted " << item << " at rear." << endl;
}

// Delete an item from the front of the deque
void Deque::deleteItemFront() {
    if (isEmpty()) {
        cout << "Queue is Underflow (No items to delete)" << endl;
        return;
    }
    int deletedItem = arr[front];
    cout << "Deleted item is " << deletedItem << endl;
    
    // Adjust front pointer
    if (front == rear) { // Only one element was present
        front = -1;
        rear = -1;
    } else {
        front++;
    }
}

// Delete an item from the rear of the deque
void Deque::deleteItemRear() {
    if (isEmpty()) {
        cout << "Queue is Underflow (No items to delete)" << endl;
        return;
    }
    int deletedItem = arr[rear];
    cout << "Deleted item is " << deletedItem << endl;
    
    // Adjust rear pointer
    if (front == rear) { // Only one element was present
        front = -1;
        rear = -1;
    } else {
        rear--;
    }
}

// Display the deque
void Deque::display() {
    if (isEmpty()) {
        cout << "Deque is empty!" << endl;
        return;
    }
    
    cout << "Deque elements: ";
    for (int i = front; i <= rear; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Check if the deque is empty
bool Deque::isEmpty() {
    return front == -1; // true if front is -1, indicating the deque is empty
}

// Main function
int main() {
    Deque deque; // Create a Deque object
    int choice, item;

    while (true) {
        cout << "\n1. Add item at front" << endl;
        cout << "2. Add item at rear" << endl;
        cout << "3. Delete item from front" << endl;
        cout << "4. Delete item from rear" << endl;
        cout << "5. Display deque" << endl;
        cout << "6. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter item to add at front: ";
                cin >> item;
                deque.addItemFront(item);
                break;
            case 2:
                cout << "Enter item to add at rear: ";
                cin >> item;
                deque.addItemRear(item);
                break;
            case 3:
                deque.deleteItemFront();
                break;
            case 4:
                deque.deleteItemRear();
                break;
            case 5:
                deque.display();
                break;
            case 6:
                cout << "Exiting..." << endl;
                return 0;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    }

    return 0;
}
