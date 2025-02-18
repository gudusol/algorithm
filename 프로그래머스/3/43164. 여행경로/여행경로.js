const answer = [];

function backTrack (tickets, visited, path, cur) {
    if (visited.length + 1 === path.length){
        answer.push([...path]);
        return;
    }
    
    for (let i = 0; i < tickets.length; i ++){
        const [depart, arrive] = tickets[i];
        
        if (!visited[i] && cur === depart){
            visited[i] = true;
            path.push(arrive);
            backTrack(tickets, visited, path, arrive);
            visited[i] = false;
            path.pop();
        }
    }
}

function solution(tickets) {
    const path = ["ICN"];
    const visited = Array.from({length: tickets.length}, () => false);

    backTrack(tickets, visited, path, "ICN");

    return answer.sort()[0]
}