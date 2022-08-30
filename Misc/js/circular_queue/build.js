// the following script is derived from https://www.youtube.com/watch?v=591-adX0F6M

class CircularQueue {
    #list;  // recall that a field started with # is a private field
    #capacity;
    #head = -1;
    #tail = -1;
    #size = 0;

    constructor(capacity) {

        // the capacity is greater than 0, and by default to be 10
        this.#capacity = Math.max(Number(capacity), 0) || 10;
        this.#list = Array(this.#capacity).fill(null);
    }

    get size() {
        return this.#size;
    }

    get isFull() {
        return this.size === this.#capacity;
    }

    get isEmpty() {
        return this.size === 0;
    }

    enqueue(item) {
        if (!this.isFull) {
            this.#tail = (this.#tail + 1) % this.#capacity;
            this.#list[this.#tail] = item;
            this.#size += 1;

            if (this.#head === -1) {
                this.#head = this.#tail;
            }
        }

        return this.size;
    }

    dequeue() {
        let item = null;

        if (!this.isEmpty) {
            item = this.#list[this.#head];
            this.#list[this.#head] = null;
            this.#head = (this.#head + 1) % this.#capacity;
            this.#size -= 1;

            if (!this.size) { // queue is empty
                this.#head = -1;
                this.#tail = -1;
            }
        }

        return item;
    }

    // peek() returns the object at the beginning of the Queue without removing it.
    peek() {
        return this.#list[this.#head];
    }

    print() {
        console.log(this.#list.filter(el => el != null))
    }
};

const cq = new CircularQueue(5);

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

// cq.dequeue()
// cq.dequeue()

// console.log(cq.peek());
// cq.print();
console.log(cq.size)
console.log(cq.isEmpty)
console.log(cq.isFull)

cq.print();