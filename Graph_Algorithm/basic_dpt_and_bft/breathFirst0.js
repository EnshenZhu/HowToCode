// The breath first traversal is mostly implemented in a iterative method

const breathFirstPrint_iterative = (graphMap, source) => {
    const queue = [source]; // use this array as a queue, and use SHIFT and PUSH to manipulate the array

    while (queue.length > 0) {
        const current = queue.shift()
        console.log(current);

        for (let neighbor of graphMap[current]) {
            queue.push(neighbor);
        };
    };

};

const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

breathFirstPrint_iterative(graph, 'a') // Anicipated result: abcdef; Real result: abcdef