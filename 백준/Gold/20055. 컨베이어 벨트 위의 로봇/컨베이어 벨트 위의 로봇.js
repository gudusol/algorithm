let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [N, K] = input[0].split(" ").map(Number);
let belt = input[1].split(" ").map(Number);

let robot = [];
up = 0;
down = N - 1;

broken = 0;
turn = 0;

while (broken < K) {
  turn++;

  up--;
  down--;
  if (up < 0) {
    up += 2 * N;
  }
  if (down < 0) {
    down += 2 * N;
  }
  if (robot && robot[0] == down) {
    robot.shift();
  }

  for (let i = 0; i < robot.length; i++) {
    let r = robot[i];
    let next = (r + 1) % (2 * N);
    if (belt[next] > 0 && !robot.includes(next)) {
      robot[i] = (robot[i] + 1) % (2 * N);
      belt[next] -= 1;
      if (belt[next] == 0) {
        broken++;
      }
    }
  }

  if (robot && robot[0] == down) {
    robot.shift();
  }

  if (belt[up] > 0) {
    robot.push(up);
    belt[up] -= 1;
    if (belt[up] == 0) {
      broken += 1;
    }
  }
}

console.log(turn);
