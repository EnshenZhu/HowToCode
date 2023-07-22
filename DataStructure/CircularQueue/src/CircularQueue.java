// Circular Queue Prototype

public class CircularQueue {
    private int capacity; // the maximum capacity of the circular queue
    private int front, rear;
    private int[] items;

    public CircularQueue(int size) {  // construct the circular queue
        this.capacity = size;
        this.front = -1;
        this.rear = -1;
        this.items = new int[capacity];
    }

    public int getFrontIdx() {
        return front;
    }

    public int getRearIdx() {
        return rear;
    }

    // Check if the CQ is empty
    public boolean isEmpty() {
        if (front == -1) {
            return true;
        } else {
            return false;
        }
    }

    // Check if the CQ is full
    public boolean isFull() {
        if (front == 0 && rear == capacity - 1) {  // the entire queue is in the normal sequence
            return true;
        }
        if (front == rear + 1) { // the last element of the queue is connected with the first element
            return true;
        }
        return false;
    }

    public void enQueue(int num) {
        if (isFull()) {
            System.out.println("The CQ is full");
        } else {
            if (front == -1) {
                front = 0;
            }
            rear = (rear + 1) % capacity;
            items[rear] = num;
            System.out.println("Inserted " + num);
        }
    }

    public void deQueue() {
        if (isEmpty()) {
            System.out.println("The CQ is empty");
        } else {
            int popElm = items[front];
            System.out.println("Removed " + popElm);

            if (front == rear) { // there is only one element in the queue
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % capacity;
            }
        }
    }
}
