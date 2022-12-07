function quick_sort(arr, start, end) {
  if (end - start < 1) {
    return;
  }
  let p = partition(arr, start, end);
  quick_sort(arr, start, p - 1);
  quick_sort(arr, p + 1, end);
}

function partition(arr, start, end) {
  let b = start;
  let p = end;
  for (let i = start; i < p; i++) {
    if (arr[i] <= arr[p]) {
      swap(arr, i, b);
      b++;
    }
  }
  swap(arr, p, b);
  return b;
}
function swap(arr, idx1, idx2) {
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  return arr;
}

let list1 = [1, 3, 5, 7, 9, 11, 13, 11];
quick_sort(list1, 0, list1.length - 1);
console.log(list1);

// 테스트 코드 2
let list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15];
quick_sort(list2, 0, list2.length - 1);
console.log(list2);

// 테스트 코드 3
let list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4];
quick_sort(list3, 0, list3.length - 1);
console.log(list3);

// const list1 = [4, 3, 6, 2, 7, 1, 5];
// const pivot_index1 = partition(list1, 0, list1.length - 1);
// console.log(list1);
// console.log(pivot_index1);

// const list2 = [6, 1, 2, 6, 3, 5, 4];
// const pivot_index2 = partition(list2, 0, list2.length - 1);
// console.log(list2);
// console.log(pivot_index2);
