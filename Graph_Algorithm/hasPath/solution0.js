// problem source: https://www.structy.net/problems/has-path

// Write a function, hasPath, that takes in an object representing the adjacency list of a directed acyclic graph and two nodes (src, dst). 
// The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

const hasPath_dft_iterative = (graphMap, src, dst) => {
    // build as an array as a stack to imply the deep first traversal with iterative method
    const stack = [src]

    while (stack.length > 0) {

        //pop out the element on the top of the stack
        const current = stack.pop();

        // if the popped-out element matches with the destination,
        // there should be path between the source to the destination
        if (current == dst) {
            return true;
        }

        // push the node's target to the stack
        for (let neighbor of graphMap[current]) {
            stack.push(neighbor);
        }
    }

    //if we finish visiting all the nodes and still cannot match with the destinaition,
    // there would be no path from the source to the destination, so we return false
    return false
}

const hasPath_dft_recursive = (graphMap, src, dst) => {
    if (src == dst) {
        return true;
    }

    for (let neighbor of graphMap[src]) {

        // if there are path from the neighbor to the destination
        // there would be definitely paths from the source to the destination
        if (hasPath_dft_recursive(graphMap, neighbor, dst) == true) {
            return true;
        };
    }

    //if we finish visiting all the nodes and still cannot match with the destinaition,
    // there would be no path from the source to the destination, so we return false
    return false
}

const hasPath_bft_iterative = (graphMap, src, dst) => {
    const queue = [src];

    while (queue.length > 0) {
        const current = queue.shift();

        if (current == dst) {
            return true;
        }

        for (let neighbor of graphMap[current]) {
            queue.push(neighbor);
        }
    }

    //if we finish visiting all the nodes and still cannot match with the destinaition,
    // there would be no path from the source to the destination, so we return false
    return false
}

const graph0 = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: []
};

const graph1 = {
    v: ['x', 'w'],
    w: [],
    x: [],
    y: ['z'],
    z: [],
};

console.log(hasPath_dft_iterative(graph0, "f", "k")) // true
console.log(hasPath_dft_iterative(graph0, "f", "j")) // false
console.log(hasPath_dft_iterative(graph0, "i", "h")) // true
console.log(hasPath_dft_iterative(graph1, "v", "w")) // true
console.log(hasPath_dft_iterative(graph1, "v", "z")) // false

// console.log(hasPath_dft_recursive(graph0, "f", "k")) // true
// console.log(hasPath_dft_recursive(graph0, "f", "j")) // false
// console.log(hasPath_dft_recursive(graph0, "i", "h")) // true
// console.log(hasPath_dft_recursive(graph1, "v", "w")) // true
// console.log(hasPath_dft_recursive(graph1, "v", "z")) // false

// console.log(hasPath_bft_iterative(graph0, "f", "k")) // true
// console.log(hasPath_bft_iterative(graph0, "f", "j")) // false
// console.log(hasPath_bft_iterative(graph0, "i", "h")) // true
// console.log(hasPath_bft_iterative(graph1, "v", "w")) // true
// console.log(hasPath_bft_iterative(graph1, "v", "z")) // false