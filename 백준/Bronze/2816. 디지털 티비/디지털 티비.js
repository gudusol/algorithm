let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const N = input.shift();

const kbs1 = input.indexOf("KBS1");
input.splice(kbs1, 1);
input.splice(0, 0, "KBS1");

const kbs2 = input.indexOf("KBS2");

answer1 = [];
answer2 = [];
for (let i = 0; i < kbs1; i++) {
  answer1.push("1");
  answer1.push("4");
}
answer1.sort();

for (let i = 0; i < kbs2; i++) {
  answer2.push("1");
  answer2.push("4");
}
answer2.sort();
answer2.pop();

console.log(answer1.join("") + answer2.join(""));
