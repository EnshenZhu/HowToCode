// Try on the O(n) Union and O(1) Find

// We will try to map the node (as the key), which belongs to the same group, into a same value

// const findAllNode = (edgeMap) => { // this function is useless

//     const allNodes = new Set(); // create an empty set to record all nodes

//     for (let neighbour of edgeMap) {

//         if (!(neighbour[0] in allNodes)) {
//             allNodes.add(element)
//         }

//         if (!(neighbour[1] in allNodes)) {
//             allNodes.add(element)
//         }

//     }

//     return Array.from(allNodes)
// }

const undirectedPath = (edgeMap, src, dst) => {
    const graphMap = findgNodeGroup(edgeMap)
    return graphMap.get(src) == graphMap.get(dst)
}

const findgNodeGroup = (edgeMap) => {
    const groupHashMap = new Map;
    // groupHashMap.set(edgeMap[0][0], edgeMap[0][0])
    // groupHashMap.set(edgeMap[0][1], edgeMap[0][0])

    // console.log(edgeMap[0][1])

    for (let idx = 0; idx < edgeMap.length; idx++) {
        if (groupHashMap.has(edgeMap[idx][1])) {
            groupHashMap.set(edgeMap[idx][0], groupHashMap.get(edgeMap[idx][1]))
        }
        else if (groupHashMap.has(edgeMap[idx][0])) {
            groupHashMap.set(edgeMap[idx][1], groupHashMap.get(edgeMap[idx][0]))
        }
        else {
            groupHashMap.set(edgeMap[idx][0], edgeMap[idx][0])
            groupHashMap.set(edgeMap[idx][1], edgeMap[idx][0])
        }
    }

    return groupHashMap

}

const edges0 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
];

// console.log(findAllNode(edges0))
// console.log(findgNodeGroup(edges0))

console.log(undirectedPath(edges0, 'j', 'm')); // -> true
console.log(undirectedPath(edges0, 'm', 'j')); // -> true
console.log(undirectedPath(edges0, 'l', 'j')); // -> true
console.log(undirectedPath(edges0, 'k', 'o')); // -> false
console.log(undirectedPath(edges0, 'i', 'o')); // -> false