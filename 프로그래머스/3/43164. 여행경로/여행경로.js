function solution(tickets) {
    const answer = [];
    const visited = Array.from({length: tickets.length}, () => false);
    
    function backTrack (path, cur) {
        if (visited.length + 1 === path.length){
            answer.push([...path]);
            return;
        }

        for (let i = 0; i < tickets.length; i ++){
            const [depart, arrive] = tickets[i];

            if (!visited[i] && cur === depart){
                visited[i] = true;
                path.push(arrive);
                backTrack(path, arrive);
                visited[i] = false;
                path.pop();
            }
        }
    }

    backTrack(["ICN"], "ICN");
    return answer.sort()[0]
}