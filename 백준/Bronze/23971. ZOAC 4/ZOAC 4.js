let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const [H, W, N, M] = input;
const a = Math.floor((H - 1) / (N + 1)) + 1;
const b = Math.floor((W - 1) / (M + 1)) + 1;

console.log(a * b);
