// A circular queue is the extended version of a regular queue where the last element is connected to the first element.
// Thus forming a circle-like structure.

// check https://www.programiz.com/dsa/circular-queue#:~:text=A%20circular%20queue%20is%20the,limitation%20of%20the%20normal%20queue.
// for more details

public class Main {
    public static void main(String[] args) {
        CircularQueue CQImplement = new CircularQueue(5);

        CQImplement.enQueue(1);
        CQImplement.enQueue(2);
        CQImplement.enQueue(3);
        CQImplement.enQueue(4);
        CQImplement.enQueue(5);
        CQImplement.enQueue(6);
        CQImplement.enQueue(7);

        CQImplement.deQueue();
        CQImplement.deQueue();

        CQImplement.enQueue(6);
        CQImplement.enQueue(7);

        CQImplement.deQueue();
        CQImplement.deQueue();
    }
}