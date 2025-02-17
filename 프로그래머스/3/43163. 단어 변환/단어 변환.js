function getDifferenceAlphabet (word1, word2) {
    let difference = 0;
    for (let i = 0; i < word1.length; i ++){
        if (word1[i] !== word2[i]){
            difference ++;
        }
    }
    return difference;
}

function bfs(target, words, current_str, current_count, visited, answer) {
    if (target === current_str) {
        answer.push(current_count);
        return;
    }
    
    for(let i = 0; i < words.length; i++){
        if (!visited[i] && getDifferenceAlphabet(current_str, words[i]) === 1){
            const new_visited = visited.slice();
            new_visited[i] = true;
            bfs(target, words, words[i], current_count + 1, new_visited, answer);
        }
    }
}


function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
    let count = 0;
    const visited = Array.from({length: words.length}, () => false);
    const answer = [];
    
    bfs(target, words, begin, count, visited, answer);
    if (answer.length > 0){
        return Math.min(...answer);
    } else {
        return 0;
    }
}