function solution(n, results) {
    let answer = 0;
    const winnerGraph = [];
    const loserGraph = [];
    
    results.forEach((result) => {
        const [winner, loser] = result;
        
        if (winnerGraph[winner]){
            winnerGraph[winner].push(loser);
        } else {
            winnerGraph[winner] = [loser];
        }
        
        if (loserGraph[loser]){
            loserGraph[loser].push(winner);
        } else {
            loserGraph[loser] = [winner];
        }
    })
    
    for (let i = 1; i <= n; i ++){
        if((bfs(winnerGraph, i) + bfs(loserGraph, i)) === n - 1){
            answer ++;
        }
    }
    
    
    function bfs(graph, start){
        const visited = Array.from({length: n + 1}, () => false);
        const queue = [start];
        visited[start] = true;
        let count = 0;
        
        while (queue.length > 0){
            const next = queue.shift();
            if(graph[next]){
                for (let i of graph[next]){
                    if (!visited[i]){
                        queue.push(i);
                        visited[i] = true;
                        count ++;
                    }
                }
            }
        }
        return count;
    }

    return answer;
}