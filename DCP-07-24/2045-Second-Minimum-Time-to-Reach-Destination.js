var secondMinimum = function(n, edges, time, change) {
    const graph = Array.from({ length: n + 1 }, () => []);
    edges.forEach(([u, v]) => {
        graph[u].push(v);
        graph[v].push(u);
    });

    const queue = [[1, 0]];
    const dist = Array.from({ length: n + 1 }, () => [Infinity, Infinity]);
    dist[1][0] = 0; 

    while (queue.length) {
        const [node, currentTime] = queue.shift();

        for (const neighbor of graph[node]) {
            let nextTime = currentTime + time;

            if (Math.floor(currentTime / change) % 2 === 1) {
                nextTime += change - (currentTime % change);
            }

            if (nextTime < dist[neighbor][0]) {
                dist[neighbor][1] = dist[neighbor][0];
                dist[neighbor][0] = nextTime;
                queue.push([neighbor, nextTime]);
            } else if (nextTime > dist[neighbor][0] && nextTime < dist[neighbor][1]) {
                dist[neighbor][1] = nextTime;
                queue.push([neighbor, nextTime]);
            }
        }
    }

    return dist[n][1]; 
};
