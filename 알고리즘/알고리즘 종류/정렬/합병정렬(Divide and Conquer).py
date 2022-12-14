def merge(list1, list2):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    i=0
    arr=[]
    while (list1!=[] and list2!=[]):
        if list1[i]>list2[i]:
            arr.append(list2[i])
            list2.remove(list2[i])
        else:
            arr.append(list1[i])
            list1.remove(list1[i])
    if list1!=[]: arr+=list1
    elif list2!=[]: arr+=list2
    return arr
# 합병 정렬
def merge_sort(my_list):
    # 여기에 코드를 작성하세요
    if len(my_list)<=1:
        return my_list
    n=len(my_list)//2
    return merge(merge_sort(my_list[:n]), merge_sort(my_list[n:]))
# 테스트 코드
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

# JS 합병정렬
# function merge(list1, list2) {
#   arr = [];
#   while (list1.length !== 0 && list2.length !== 0) {
#     if (list1[0] > list2[0]) {
#       arr.push(list2[0]);
#       list2.shift();
#     } else {
#       arr.push(list1[0]);
#       list1.shift();
#     }
#   }
#   if (list1.length === 0) {
#     arr.push(...list2);
#   } else {
#     arr.push(...list1);
#   }
#   return arr;
# }
# function merge_sort(my_list) {
#   if (my_list.length === 1) {
#     return my_list;
#   }
#   const n = Math.ceil(my_list.length / 2);
#   const left = my_list.slice(0, n);
#   const right = my_list.slice(n);
#   return merge(merge_sort(left), merge_sort(right));
# }
# console.log(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]));
# console.log(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]));
# console.log(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]));
