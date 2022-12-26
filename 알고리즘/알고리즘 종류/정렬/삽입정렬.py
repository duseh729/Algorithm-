def selection_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            # 불필요한 비교를 막기 위함.
            else:break
    return arr
arr=list(map(int, input().split()))
print(selection_sort(arr))
# 바꿀 값을 왼쪽과 비교해 값이 왼쪽보다 크면 스왑

# js 삽입정렬
# function selection_sort(arr) {
#   for (let i = 1; i < arr.length; i++) {
#     for (let j = arr.length; j > 0; j--) {
#       if (arr[j] < arr[j - 1]) {
#         [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
#       }
#     }
#   }
#   return arr;
# }
# console.log(selection_sort([3, 4, 5, 1, 2, 3, 4]));
