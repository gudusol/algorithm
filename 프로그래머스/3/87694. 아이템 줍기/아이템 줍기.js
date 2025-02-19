


function solution(rectangle, characterX, characterY, itemX, itemY) {
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    const board = [];
    const maxX = (Math.max(...rectangle.map((rec) => rec[2])) + 1) * 2;
    const maxY = (Math.max(...rectangle.map((rec) => rec[3])) + 1) * 2;
    
    for (let i = 0; i < maxX; i ++){
        board.push(Array.from({length: maxY}, () => 0));
    }
    
    for (let rec of rectangle){
        const [leftX, leftY, rightX, rightY] = rec.map((v) => v * 2);
        for (let x = leftX; x <= rightX; x ++){
            for (let y = leftY; y <= rightY; y++){
                board[x][y] = Infinity;
            }
        }
    }
    
    for (let rec of rectangle){
        const [leftX, leftY, rightX, rightY] = rec.map((v) => v * 2);
        for (let x = leftX + 1; x < rightX; x ++){
            for (let y = leftY + 1; y < rightY; y++){
                board[x][y] = 0;
            }
        }
    }
    
    const [startX, startY] = [characterX * 2, characterY * 2];
    board[startX][startY] = 1; 
    const queue = [[startX, startY]];
    while (queue.length > 0){
        const [curX, curY] = queue.shift();
        if (curX === itemX * 2 && curY === itemY * 2) {
            return Math.floor(board[curX][curY] / 2);
        }
        for (let i = 0; i < 4; i ++){
            const [nextX, nextY] = [curX + dx[i], curY + dy[i]];
            if (board[nextX][nextY] === Infinity) {
                queue.push([nextX, nextY]);
                board[nextX][nextY] = board[curX][curY] + 1;
            }
        }
    }
}