#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

// Data structure for student information, i.e., node
struct Node {
    int prn;
    char name[20];
    Node *next;
};

class Panclub {
    int num, cnt;
    char nm[20];  // Data members
    Node *head;   // Pointing to first node

public:
    Panclub() { // Constructor to initialize object
        num = cnt = 0;
        head = NULL;
    }

    Node *create();
    void display(Node *);
    Node *concat(Node *, Node *);  // Member Functions with arguments
    void reverse(Node *);
    Node* insert_president(Node *);
    void insert_sec(Node *);
    void insert_member(Node *);
    Node* del_president(Node *);
    Node* del_secretary(Node *);
    Node* del_member(Node *);
};

// To Create the list of Divisions
Node* Panclub::create() {
    Node *temp, *n1;
    temp = n1 = NULL;

    cout << "\nHow many students data do you want to insert in the panclub database: ";
    cin >> cnt;

    do {
        n1 = new Node; // Allocate memory for all fields of struct
        cout << "\nEnter the PRN number of student: ";
        cin >> num;
        n1->prn = num; // Storing the PRN in node field prn
        cout << "\nEnter the name of student: ";
        cin >> nm;
        strcpy(n1->name, nm); // Storing the name in node field name
        n1->next = NULL; // Making the next field null

        if (head == NULL) { // Check if head is empty
            head = n1; // Make new node as head
            temp = head;
        } else {
            temp = head;
            while (temp->next != NULL) // Attach at the end of list
                temp = temp->next;
            temp->next = n1;
        }
        cnt--;
    } while (cnt > 0);

    return head;
}

void Panclub::display(Node *head) { // Display the list of both divisions
    Node *temp = head;
    while (temp != NULL) {
        cout << "[" << temp->prn << "|" << temp->name << "]->";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

Node* Panclub::concat(Node *head1, Node *head2) { // Concatenate both divisions
    Node *head3, *temp;
    head3 = temp = NULL;

    if (head1 == NULL) return head2; // If first list is empty, return second list
    if (head2 == NULL) return head1; // If second list is empty, return first list

    head3 = head1;
    temp = head3;

    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = head2; // Append the second list at the end of the first

    return head3;
}

void Panclub::reverse(Node *head) {
    if (head == NULL) return;
    reverse(head->next);
    cout << "[" << head->prn << "|" << head->name << "]->";
}

Node* Panclub::insert_president(Node *head) {
    Node *n2 = new Node;
    cout << "\nEnter the PRN number of President: ";
    cin >> n2->prn;
    cout << "\nEnter the name of President: ";
    cin >> n2->name;
    n2->next = head; // Insert at the beginning
    head = n2;
    return head;
}

void Panclub::insert_sec(Node *head) {
    Node *temp, *n2 = new Node;
    cout << "\nEnter the PRN number of Secretary: ";
    cin >> n2->prn;
    cout << "\nEnter the Name of Secretary: ";
    cin >> n2->name;
    n2->next = NULL;

    temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = n2; // Insert at the end
}

Node* Panclub::del_president(Node *head) {
    Node *temp = head;
    if (temp != NULL) {
        head = temp->next;
        delete temp;
    }
    return head;
}

Node* Panclub::del_secretary(Node *head) {
    Node *temp = head, *t1 = NULL;
    if (temp == NULL) return head; // No nodes to delete

    while (temp->next != NULL) {
        t1 = temp; // Keep track of the previous node
        temp = temp->next;
    }
    if (t1 != NULL) t1->next = NULL; // Remove last node
    delete temp;
    return head;
}

Node* Panclub::del_member(Node *head) {
    Node *temp = head, *t1 = NULL;
    int pn;
    cout << "\nEnter the PRN number after which you want to delete the member: ";
    cin >> pn;

    while (temp != NULL) {
        if (temp->prn == pn) {
            t1 = temp->next;
            if (t1 != NULL) {
                temp->next = t1->next; // Bypass the node to be deleted
                delete t1; // Free memory
            }
            cout << "\n\nMember removed successfully!" << endl;
            return head;
        }
        temp = temp->next;
    }
    cout << "\nPRN not found!" << endl;
    return head;
}

int main() {
    Panclub p1, p2, p3;
    Node *h1, *h2, *h3;
    h1 = h2 = h3 = NULL;
    int ch;

    cout << "\n\t!!!Group B: Assignment No: 01!!!" << endl; // prints assignment number and group
    do {
        cout << "\n1. Enter data of SE A Division:";
        cout << "\n2. Enter data of SE B Division:";
        cout << "\n3. Concatenation of Lists..";
        cout << "\nEnter your choice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cout << "\n\nPlease enter the student info who is registered member.." << endl;
                cout << "\nEnter the Panclub Data of SE A Division:\n";
                h1 = p1.create();
                cout << "\nSE Comp Division A List are as follows..\n";
                p1.display(h1);
                cout << "\nReverse List of SE Div A:\n";
                p1.reverse(h1);
                p1.insert_sec(h1);
                cout << "\nAfter insertion of Secretary: \n";
                p1.display(h1);
                h1 = p1.insert_president(h1);
                cout << "\nAfter insertion of President: \n";
                p1.display(h1);
                p1.insert_member(h1);
                cout << "\nAfter insertion of member...\n";
                p1.display(h1);
                h1 = p1.del_president(h1);
                cout << "\nAfter deletion of president...\n";
                p1.display(h1);
                h1 = p1.del_secretary(h1);
                cout << "\nAfter deletion of secretary...\n";
                p1.display(h1);
                h1 = p1.del_member(h1);
                cout << "\nAfter deletion of member...\n";
                p1.display(h1);
                break;

            case 2:
                cout << "\nEnter the Panclub Data of SE B Division:\n";
                h2 = p2.create();
                cout << "\nSE Comp Division B List are as follows..\n";
                p2.display(h2);
                cout << "\nReverse List of SE Div B:\n";
                p2.reverse(h2);
                p2.insert_sec(h2);
                cout << "\nAfter insertion of Secretary: \n";
                p2.display(h2);
                h2 = p2.insert_president(h2);
                cout << "\nAfter insertion of President: \n";
                p2.display(h2);
                p2.insert_member(h2);
                cout << "\nAfter insertion of member...\n";
                p2.display(h2);
                h2 = p2.del_president(h2);
                cout << "\nAfter deletion of president...\n";
                p2.display(h2);
                h2 = p2.del_secretary(h2);
                cout << "\nAfter deletion of secretary...\n";
                p2.display(h2);
                h2 = p2.del_member(h2);
                cout << "\nAfter deletion of member...\n";
                p2.display(h2);
                break;

            case 3:
                h3 = p3.concat(h1, h2);
                cout << "\nThe concatenation of Div: A and Div: B of SE Comp Class are as follows:\n";
                p3.display(h3);
                break;

            default:
                cout << "Invalid choice! Please try again." << endl;
                break;
        }
    } while (ch != 4);
    
    return 0;
}
