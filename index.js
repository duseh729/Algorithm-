let myArr = [
  [1, 4],
  [3, 5],
  [0, 6],
  [5, 7],
  [3, 8],
  [5, 9],
  [6, 10],
  [8, 11],
  [8, 12],
  [2, 13],
  [12, 14],
];
console.log(myArr);
myArr.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  } else {
    return a[1] - b[1];
  }
});
console.log(myArr);
let answer = [];
answer.push(myArr[0]);
for (i of myArr) {
  if (i[0] > answer[answer.length - 1][1]) {
    answer.push(i);
  }
}
console.log(answer);
