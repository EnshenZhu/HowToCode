// This case has O(1) Union and O(n) Find

// Write a function, undirectedPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB).
// The function should return a boolean indicating whether there exists a path between nodeA and nodeB.

const undirectedPath = (edgesMap, nodeA, nodeB) => {
    const graphMap = buildGraph(edgesMap)
    // console.log(graphMap)
    return hasPath(graphMap, nodeA, nodeB, new Set());
    // Set objects are collections of values. A value in the Set may only occur once; 
    // it is unique in the Set's collection. You can iterate through the elements of a set in insertion order.
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
}

const hasPath = (graphMap, src, dst, visited) => { // 'visited' is a hash set
    if (src == dst) return true;
    if (visited.has(src)) return false; // there is no reason to travel from a visited node

    visited.add(src) // add the source to the visited set

    // if there are path from the neighbor to the destination,
    // there would be definitely paths from the source to the destination.
    for (let neighbor of graphMap[src]) {
        if (hasPath(graphMap, neighbor, dst, visited) == true) {
            return true;
        }
    }

    // if we finish visiting all the nodes and still cannot match with the destinaition,
    // there would be no path from the source to the destination, so we return false
    return false;
}

const buildGraph = (edgesMap) => { // also known as Union 
    const graphMap = {};

    // iterating through every single edges
    for (let singleEdge of edgesMap) {
        const [a, b] = singleEdge; // destructure each edges pairs

        // we then initialize the nodes to the key of objects
        if (!(a in graphMap)) graphMap[a] = [];
        if (!(b in graphMap)) graphMap[b] = [];

        // add the directed path to the a and b
        graphMap[a].push(b);
        graphMap[b].push(a);
    }

    return graphMap;
};

const edges0 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
];

const edges1 = [
    ['b', 'a'],
    ['c', 'a'],
    ['b', 'c'],
    ['q', 'r'],
    ['q', 's'],
    ['q', 'u'],
    ['q', 't'],
];

const edges2 = [
    ['s', 'r'],
    ['t', 'q'],
    ['q', 'r'],
];

console.log(undirectedPath(edges0, 'j', 'm')); // -> true


console.log(undirectedPath(edges0, 'm', 'j')); // -> true
console.log(undirectedPath(edges0, 'l', 'j')); // -> true
console.log(undirectedPath(edges0, 'k', 'o')); // -> false
console.log(undirectedPath(edges0, 'i', 'o')); // -> false

console.log(undirectedPath(edges1, 'a', 'b')); // -> true
console.log(undirectedPath(edges1, 'a', 'c')); // -> true
console.log(undirectedPath(edges1, 'r', 't')); // -> true
console.log(undirectedPath(edges1, 'r', 'b')); // -> false

console.log(undirectedPath(edges2, 'r', 't')); // -> true
