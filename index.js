function consecutive_sum(start, end) {
  if (start === end) {
    return start;
  }
  const mid = parseInt((start + end) / 2);
  return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end);
}
console.log(consecutive_sum(1, 10));
console.log(consecutive_sum(1, 100));
console.log(consecutive_sum(1, 253));
console.log(consecutive_sum(1, 388));
