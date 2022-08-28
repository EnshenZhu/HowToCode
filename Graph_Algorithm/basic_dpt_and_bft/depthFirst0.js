// We can use either iterative method or recursive method to solve the depth first traversal

const depthFirstPrint_iterative = (graphMap, source) => {
    const stack = [source]; // use this array as a stack, and use push and pop to manipulate the array

    // we will continue the while loop as long as the stack is NOT empty
    while (stack.length > 0) {
        const current = stack.pop();
        console.log(current);

        for (let neighbor of graphMap[current]) {
            stack.push(neighbor);
        }
    }
};

// In the recursive method, we do not need extra space to exactly store the stack
const depthFirstPrint_recursive = (graphMap, source) => {
    console.log(source);
    for (let neightbor of graphMap[source]){
        depthFirstPrint_recursive(graphMap,neightbor)
    }
}

const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

// depthFirstPrint_iterative(graph, 'a') // Anicipated result: abdfce; Real result: acebdf
depthFirstPrint_recursive(graph, 'a') // Anicipated result: abdfce; Real result: abdfce