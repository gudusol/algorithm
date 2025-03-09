let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((s) => s.split(" ").map(Number));

input.pop();
for (let numbers of input) {
  const [num1, num2, num3] = numbers.sort((a, b) => a - b);

  if (num1 + num2 <= num3) {
    console.log("Invalid");
  } else if (num1 === num2 && num2 === num3) {
    console.log("Equilateral");
  } else if (num1 !== num2 && num2 !== num3 && num1 !== num3) {
    console.log("Scalene");
  } else {
    console.log("Isosceles");
  }
}
