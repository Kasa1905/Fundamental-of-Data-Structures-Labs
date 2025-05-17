/*Queues are frequently used in computer programming, and a typical example is the creation of a job queue by an operating system. If the operating system does not use priorities, thenthe jobs are processed in the order they enter the system. Write C++ program for simulating job queue. Write functions to add job and delete job from queue*/ 

#include <iostream>
#define MAX 10
using namespace std;

struct queue
{
    int data[MAX];
    int front, rear;
};

class Queue
{
    struct queue q;
public:
    Queue() { q.front = q.rear = -1; }
    int isempty();
    int isfull();
    void enqueue(int x);
    int delqueue();
    void display();
};

int Queue::isempty()
{
    return (q.front == q.rear) ? 1 : 0;
}

int Queue::isfull()
{
    return (q.rear == MAX - 1) ? 1 : 0;
}

void Queue::enqueue(int x)
{
    if (isfull())
    {
        cout << "Queue is overflow" << endl;
        return;
    }
    q.data[++q.rear] = x;
}

int Queue::delqueue()
{
    if (isempty())
    {
        cout << "Queue is underflow" << endl;
        return -1;
    }
    return q.data[++q.front];
}

void Queue::display()
{
    if (isempty())
    {
        cout << "Queue is empty" << endl;
        return;
    }
    cout << "\n";
    for (int i = q.front + 1; i <= q.rear; i++)
        cout << q.data[i] << " ";
    cout << endl;
}

int main()
{
    cout << "TEJAS NALAWADE SCOD09" << endl;
    Queue obj;
    int ch, x;
    do
    {
        cout << "\n 1.insert job\n 2.delete job\n 3.display\n 4.Exit\n Enter your choice:";
        cin >> ch;
        switch (ch)
        {
        case 1:
            if (!obj.isfull())
            {
                cout << "\n Enter data:";
                cin >> x;
                obj.enqueue(x);
            }
            else
                cout << "Queue is overflow";
            break;
        case 2:
            if (!obj.isempty())
            {
                cout << "\n Deleted Element=" << obj.delqueue();
                cout << "\nremaining jobs :";
                obj.display();
            }
            else
            {
                cout << "\n Queue is underflow";
            }
            break;
        case 3:
            obj.display();
            break;
        case 4:
            cout << "\n Exit";
            break;
        default:
            cout << "\nInvalid choice!";
        }
    } while (ch != 4);
    return 0;
}
