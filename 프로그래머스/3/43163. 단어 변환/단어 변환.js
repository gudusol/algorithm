function checkAlphabet (word1, word2) {
    let difference = 0;
    for (let i = 0; i < word1.length; i ++){
        if (word1[i] !== word2[i]){
            difference ++;
        }
    }
    return difference === 1;
}


function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
    const visited = Array.from({length: words.length}, () => false);
    const queue = [[begin, 0]];
    
    while (queue.length > 0){
        const [cur_str, cur_count] = queue.shift();
        if (cur_str === target){
            return cur_count;
        }
        
        for (let i = 0; i < words.length; i ++){
            if(!visited[i] && checkAlphabet(cur_str, words[i])) {
                visited[i] = true;
                queue.push([words[i], cur_count + 1]);
            }
        }
    }
}