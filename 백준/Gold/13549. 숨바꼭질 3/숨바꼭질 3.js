let [N, K] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const MAX_LENGTH = 100001;

let arr = Array(MAX_LENGTH).fill(Infinity);
let visited = Array(MAX_LENGTH).fill(false);

arr[N] = 0;
visited[N] = true;

let que = [N];

while (que.length > 0) {
  let cur = que.shift();

  if (cur * 2 < MAX_LENGTH && !visited[cur * 2]) {
    que.unshift(cur * 2);
    arr[cur * 2] = arr[cur];
    visited[cur * 2] = true;
  }

  if (cur - 1 >= 0 && !visited[cur - 1]) {
    que.push(cur - 1);
    arr[cur - 1] = arr[cur] + 1;
    visited[cur - 1] = true;
  }

  if (cur + 1 < MAX_LENGTH && !visited[cur + 1]) {
    que.push(cur + 1);
    arr[cur + 1] = arr[cur] + 1;
    visited[cur + 1] = true;
  }
}

console.log(arr[K]);
