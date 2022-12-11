def course_selection(course_list):
    # 여기에 코드를 작성하세요
    course_list=sorted(course_list,key=lambda x: x[1])
    answer=[]
    answer.append(course_list[0])
    for i in course_list:
        if i[0]>answer[-1][1]:
            answer.append(i)
    return answer

# 테스트 코드
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

# js
# function course_selection(course_list) {
#   course_list.sort((a, b) => {
#     if (a[1] === b[1]) {
#       return a[0] - b[0];
#     } else {
#       return a[1] - b[1];
#     }
#   });
#   answer = [];
#   answer.push(course_list[0]);
#   for (i of course_list) {
#     if (i[0] >= answer[answer.length - 1][1]) {
#       answer.push(i);
#     }
#   }
#   return answer;
# }

# console.log(
#   course_selection([
#     [6, 10],
#     [2, 3],
#     [4, 5],
#     [1, 7],
#     [6, 8],
#     [9, 10],
#   ])
# );
# // console.log(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]));
# // console.log(
# //   course_selection([
# //     (4, 7),
# //     (2, 5),
# //     (1, 3),
# //     (8, 10),
# //     (5, 9),
# //     (2, 5),
# //     (13, 16),
# //     (9, 11),
# //     (1, 8),
# //   ])
# // );
