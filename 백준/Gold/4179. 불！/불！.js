let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [R, C] = input[0].split(" ").map((e) => +e);
board = Array.from({ length: R + 2 }, () => Array(C + 2).fill(0));
visited = Array.from({ length: R + 2 }, () => Array(C + 2).fill(false));

const MAX_INT = Infinity;

dx = [-1, 0, 1, 0];
dy = [0, 1, 0, -1];

const que = [];
let [x, y] = [0, 9];

for (let row = 1; row < R + 1; row++) {
  line = input[row];
  for (let col = 1; col < line.length + 1; col++) {
    let s = line[col - 1];

    if (s === "J") {
      x = row;
      y = col;
      board[row][col] = MAX_INT;
    } else if (s === ".") {
      board[row][col] = MAX_INT;
    } else if (s === "F") {
      que.push([row, col]);
      board[row][col] = 0;
    } else {
      board[row][col] = -1;
    }
  }
}

while (que.length > 0) {
  const [cur_x, cur_y] = que.shift();

  for (let i = 0; i < 4; i++) {
    const next_x = cur_x + dx[i];
    const next_y = cur_y + dy[i];

    if (board[next_x][next_y] === MAX_INT) {
      board[next_x][next_y] = board[cur_x][cur_y] + 1;
      que.push([next_x, next_y]);
    }
  }
}

que.push([x, y, 0]);
visited[x][y] = true;
let is_end = false;

while (que.length > 0) {
  const [cur_x, cur_y, time] = que.shift();

  if (cur_x === 1 || cur_y === 1 || cur_x === R || cur_y === C) {
    console.log(time + 1);
    is_end = true;
    break;
  }

  for (let i = 0; i < 4; i++) {
    const next_x = cur_x + dx[i];
    const next_y = cur_y + dy[i];

    if (!visited[next_x][next_y] && board[next_x][next_y] > time + 1) {
      visited[next_x][next_y] = true;
      que.push([next_x, next_y, time + 1]);
    }
  }
}

if (!is_end) {
  console.log("IMPOSSIBLE");
}
