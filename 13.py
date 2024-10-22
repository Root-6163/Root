#include <iostream>
using namespace std;

#define MAX 5 // Maximum number of orders

class CircularQueue {
private:
    int orders[MAX]; // Array to store orders
    int front;       // Front index
    int rear;        // Rear index

public:
    CircularQueue(); // Constructor to initialize the circular queue
    void placeOrder(int order); // Place an order
    void serveOrder();          // Serve the next order
    void displayOrders();       // Display all orders
    bool isFull();             // Check if the queue is full
    bool isEmpty();            // Check if the queue is empty
};

// Constructor to initialize front and rear
CircularQueue::CircularQueue() {
    front = -1;
    rear = -1;
}

// Check if the circular queue is full
bool CircularQueue::isFull() {
    return (front == (rear + 1) % MAX);
}

// Check if the circular queue is empty
bool CircularQueue::isEmpty() {
    return (front == -1);
}

// Place an order in the circular queue
void CircularQueue::placeOrder(int order) {
    if (isFull()) {
        cout << "Circular Queue Overflow: Cannot place order " << order << endl;
        return;
    }
    if (front == -1) { // First order being placed
        front = 0;
    }
    rear = (rear + 1) % MAX; // Circular increment of rear
    orders[rear] = order;    // Add the order to the queue
    cout << "Order " << order << " placed." << endl;
}

// Serve the next order from the circular queue
void CircularQueue::serveOrder() {
    if (isEmpty()) {
        cout << "Circular Queue Underflow: No orders to serve." << endl;
        return;
    }
    int servedOrder = orders[front]; // Get the order to be served
    cout << "Serving order " << servedOrder << endl;
    
    // If there's only one order left
    if (front == rear) {
        front = -1; // Reset queue
        rear = -1;
    } else {
        front = (front + 1) % MAX; // Circular increment of front
    }
}

// Display all orders in the circular queue
void CircularQueue::displayOrders() {
    if (isEmpty()) {
        cout << "No orders in the queue." << endl;
        return;
    }

    cout << "Current orders in the queue: ";
    int i = front;
    while (true) {
        cout << orders[i] << " ";
        if (i == rear) break; // Exit loop when reaching the rear
        i = (i + 1) % MAX;    // Circular increment
    }
    cout << endl;
}

// Main function
int main() {
    CircularQueue pizzaQueue; // Create a CircularQueue object
    int choice, order;

    while (true) {
        cout << "\nPizza Parlor Order System" << endl;
        cout << "1. Place an Order" << endl;
        cout << "2. Serve an Order" << endl;
        cout << "3. Display Orders" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter order number: ";
                cin >> order;
                pizzaQueue.placeOrder(order);
                break;
            case 2:
                pizzaQueue.serveOrder();
                break;
            case 3:
                pizzaQueue.displayOrders();
                break;
            case 4:
                cout << "Exiting..." << endl;
                return 0;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    }

    return 0;
}

