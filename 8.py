#include <iostream>
using namespace std;

// Define the structure for a singly linked list node
struct SLLNode {
    char data;
    SLLNode* next;
};

// Function prototypes
SLLNode* createSLL(int cnt);
void displaySLL(SLLNode* head);
void A_U_B(SLLNode* headA, SLLNode* headB);
void A_int_B(SLLNode* headA, SLLNode* headB);
void A_Min_B(SLLNode* headA, SLLNode* headB);
void B_Min_A(SLLNode* headA, SLLNode* headB);
void U_Min_A_U_B(SLLNode* headU, SLLNode* headA, SLLNode* headB);
void freeSLL(SLLNode* head); // Function to free memory

int main() {
    int no;
    cout << "\n\n\t How many Linked Lists: ";
    cin >> no;

    // Create heads for the three linked lists
    SLLNode* headU = nullptr;
    SLLNode* headA = nullptr;
    SLLNode* headB = nullptr;

    for (int i = 1; i <= no; i++) {
        if (i == 1) {
            cout << "\n\n\t Enter 10 Students of SE Comp: ";
            headU = createSLL(10);
            cout << "\n";
            displaySLL(headU);
        }
        if (i == 2) {
            cout << "\n\n\t Enter 5 Students who like Vanilla Icecream: ";
            headA = createSLL(5);
            cout << "\n";
            displaySLL(headA);
        }
        if (i == 3) {
            cout << "\n\n\t Enter 5 Students who like Butterscotch Icecream: ";
            headB = createSLL(5);
            cout << "\n";
            displaySLL(headB);
        }
    }

    // Display input sets
    cout << "\n\n Input Sets:------------------------";
    cout << "\n\n Set 'U': ";
    displaySLL(headU);
    cout << "\n\n Set 'A': ";
    displaySLL(headA);
    cout << "\n\n Set 'B': ";
    displaySLL(headB);

    // Perform set operations
    cout << "\n\n Output Sets:------------------------";
    A_U_B(headA, headB);
    A_int_B(headA, headB);
    A_Min_B(headA, headB);
    B_Min_A(headA, headB);
    U_Min_A_U_B(headU, headA, headB);

    // Free memory
    freeSLL(headU);
    freeSLL(headA);
    freeSLL(headB);

    cout << "\n\n";
    return 0;
}

// Function to create a singly linked list
SLLNode* createSLL(int cnt) {
    SLLNode* head = nullptr;
    SLLNode* tail = nullptr;

    for (int i = 0; i < cnt; i++) {
        SLLNode* newNode = new SLLNode; // Allocate memory for a new node
        cout << "\n\t Enter Student Initial: ";
        cin >> newNode->data;
        newNode->next = nullptr;

        if (head == nullptr) { // First node
            head = newNode;
            tail = head;
        } else { // Append to the list
            tail->next = newNode;
            tail = tail->next;
        }
    }
    return head;
}

// Function to display a linked list
void displaySLL(SLLNode* head) {
    SLLNode* current = head;
    while (current != nullptr) {
        cout << " " << current->data;
        current = current->next;
    }
}

// Function for Set A U B
void A_U_B(SLLNode* headA, SLLNode* headB) {
    char a[15]; // Increased size for union
    int i = 0;
    SLLNode* p = headA;
    SLLNode* q = headB;

    // Copy elements from Set A
    while (p != nullptr) {
        a[i++] = p->data;
        p = p->next;
    }

    // Copy elements from Set B, avoiding duplicates
    while (q != nullptr) {
        bool exists = false;
        for (int j = 0; j < i; j++) {
            if (a[j] == q->data) {
                exists = true;
                break;
            }
        }
        if (!exists) {
            a[i++] = q->data;
        }
        q = q->next;
    }

    cout << "\n\n\t Set A U B: ";
    for (int j = 0; j < i; j++) {
        cout << " " << a[j];
    }
}

// Function for Set A ∩ B
void A_int_B(SLLNode* headA, SLLNode* headB) {
    char a[10];
    int i = 0;
    SLLNode* p = headA;

    while (p != nullptr) {
        SLLNode* q = headB;
        while (q != nullptr) {
            if (p->data == q->data) {
                a[i++] = p->data;
                break;
            }
            q = q->next;
        }
        p = p->next;
    }

    cout << "\n\n\t Set A ∩ B: ";
    for (int j = 0; j < i; j++) {
        cout << " " << a[j];
    }
}

// Function for Set A - B
void A_Min_B(SLLNode* headA, SLLNode* headB) {
    char a[10];
    int i = 0;
    SLLNode* p = headA;

    while (p != nullptr) {
        bool exists = false;
        SLLNode* q = headB;
        while (q != nullptr) {
            if (p->data == q->data) {
                exists = true;
                break;
            }
            q = q->next;
        }
        if (!exists) {
            a[i++] = p->data;
        }
        p = p->next;
    }

    cout << "\n\n\t Set A - B: ";
    for (int j = 0; j < i; j++) {
        cout << " " << a[j];
    }
}

// Function for Set B - A
void B_Min_A(SLLNode* headA, SLLNode* headB) {
    char a[10];
    int i = 0;
    SLLNode* q = headB;

    while (q != nullptr) {
        bool exists = false;
        SLLNode* p = headA;
        while (p != nullptr) {
            if (q->data == p->data) {
                exists = true;
                break;
            }
            p = p->next;
        }
        if (!exists) {
            a[i++] = q->data;
        }
        q = q->next;
    }

    cout << "\n\n\t Set B - A: ";
    for (int j = 0; j < i; j++) {
        cout << " " << a[j];
    }
}

// Function for Set U - (A U B)
void U_Min_A_U_B(SLLNode* headU, SLLNode* headA, SLLNode* headB) {
    char a[15]; // Increased size for U - (A U B)
    int i = 0;
    SLLNode* p = headU;

    while (p != nullptr) {
        bool exists = false;

        // Check existence in A
        SLLNode* q = headA;
        while (q != nullptr) {
            if (p->data == q->data) {
                exists = true;
                break;
            }
            q = q->next;
        }

        // Check existence in B
        if (!exists) {
            q = headB;
            while (q != nullptr) {
                if (p->data == q->data) {
                    exists = true;
                    break;
                }
                q = q->next;
            }
        }

        // If not in A or B, add to the result
        if (!exists) {
            a[i++] = p->data;
        }
        p = p->next;
    }

    cout << "\n\n\t Set U - (A U B): ";
    for (int j = 0; j < i; j++) {
        cout << " " << a[j];
    }
}

// Function to free memory of linked list
void freeSLL(SLLNode* head) {
    SLLNode* current = head;
    while (current != nullptr) {
        SLLNode* next = current->next;
        delete current;
        current = next;
    }
}
