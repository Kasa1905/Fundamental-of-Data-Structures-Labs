#include <iostream>
#define MAX 10

using namespace std;

struct myQueue {
    int data[MAX];
    int front, rear;
};

class Queue {
    struct myQueue q;
public:
    Queue() { q.front = q.rear = -1; }
    bool is_empty() { return q.front == -1; }
    bool is_full() { return q.rear == MAX - 1; }
    void enqueue(int x) {
        if (is_full()) {
            cout << "Queue is full!" << endl;
        } else {
            q.data[++q.rear] = x;
        }
    }
    int dequeue() {
        if (is_empty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        } else {
            return q.data[++q.front];
        }
    }
    void display() {
        if (is_empty()) {
            cout << "Queue is empty!" << endl;
        } else {
            for (int i = q.front + 1; i <= q.rear; i++) {
                cout << q.data[i] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    Queue obj;
    int ch, x;
    do {
        cout << "\n 1. Insert Job\n 2. Delete Job\n 3. Display\n 4. Exit\n";
        cout << "Enter your choice: ";
        cin >> ch;
        switch (ch) {
            case 1:
                if (!obj.is_full()) {
                    cout << "Enter data: ";
                    cin >> x;
                    obj.enqueue(x);
                } else {
                    cout << "Queue is full!" << endl;
                }
                break;
            case 2:
                if (!obj.is_empty()) {
                    cout << "Deleted Element = " << obj.dequeue() << endl;
                } else {
                    cout << "Queue is empty!" << endl;
                }
                break;
            case 3:
                obj.display();
                break;
            case 4:
                cout << "Exiting Program..." << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
        }
    } while (ch != 4);
    return 0;
}