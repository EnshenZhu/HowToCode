const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

breathFirstPrint_iterative(graph, 'a') // Anicipated result: abcdef; Real result: abdfce