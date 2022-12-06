def selection_sort(arr):
    #마지막 인덱스는 비교 안해도 되기 때문에 -1
    for i in range(len(arr) - 1):
        min_idx = i
        #i인덱스 값끼리는 비교 안해도 돼서 i+1 부터 시작.
        for j in range(i + 1, len(arr)):
            #배열에서 제일 작은 값인덱스를 저장
            if arr[j] < arr[min_idx]:
                min_idx = j
        #제일 작은 값인덱스와 i인덱스값 스왑
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr=list(map(int, input().split()))
print(selection_sort(arr))
# 선택정렬은 배열[0]~배열[끝]까지 작은 값을 찾아서 
# 배열의 처음부터 순서대로 넣어주는 것.

# js 선택정렬
# function selection_sort(arr) {
#   for (let i = 0; i < arr.length; i++) {
#     min_idx = i;
#     for (let j = i + 1; j < arr.length; j++) {
#       if (arr[min_idx] > arr[j]) {
#         min_idx = j;
#       }
#     }
#     [arr[min_idx], arr[i]] = [arr[i], arr[min_idx]];
#   }
#   return arr;
# }
# console.log(selection_sort([3, 4, 5, 1, 2, 3, 4]));
