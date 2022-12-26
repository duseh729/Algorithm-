# 버블정렬 구현
# for랑 if문 조건이 빈 칸 이었음

def solution(num_list):
    for n in range(len(num_list)):
        for i in range(len(num_list)-1):
            if num_list[i]>num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

    return num_list