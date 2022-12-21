# 11651
# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 
# 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n=int(input())
k=[]
for _ in range(n):
    k.append(list(map(int, input().split())))
# 파이썬 정렬 함수
k.sort(key=lambda x:(x[1], x[0]))

for i in k:
    print(i[0], end=' ')
    print(i[1])

# 입력
# 5
# 0 4 
# 1 2
# 1 -1
# 2 2
# 3 3
# 출력
# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4