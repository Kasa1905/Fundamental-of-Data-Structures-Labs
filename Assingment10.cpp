#include <iostream>
#include <string>

using namespace std;

const int MAX_SIZE = 20;

struct Stack {
    int top;
    int array[MAX_SIZE];
};

void initialize(Stack& st) {
    st.top = -1;
}

bool isFull(Stack& st) {
    return st.top >= MAX_SIZE - 1;
}

bool isEmpty(Stack& st) {
    return st.top == -1;
}

void push(Stack& st, int num) {
    if (isFull(st)) {
        cout << "Stack is full." << endl;
    } else {
        st.array[++st.top] = num;
    }
}

int pop(Stack& st) {
    if (isEmpty(st)) {
        cout << "Stack is empty." << endl;
        return -1;
    } else {
        return st.array[st.top--];
    }
}

int main() {
    Stack st;
    initialize(st);

    string inputString;
    cout << "Enter a string of parentheses: ";
    cin >> inputString;

    int length = inputString.length();
    for (int i = 0; i < length; i++) {
        if (inputString[i] == '{') {
            push(st, inputString[i]);
        } else if (inputString[i] == '}') {
            if (isEmpty(st)) {
                printf("Error: Invalid character !!\n");
                return 0;
            }
            pop(st);
        } else {
            printf("Error: Invalid character !!\n");
            return 0;
        }
    }

    if (isEmpty(st)) {
        printf("Valid Paranthesis Expression\n");
    } else {
        printf("Invalid Paranthesis Expression\n");
    }

    return 0;
}