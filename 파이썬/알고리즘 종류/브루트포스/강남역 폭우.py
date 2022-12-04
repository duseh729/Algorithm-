def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height

# 테스트 코드
print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# 예를 들어서 파라미터 buildings로 
# [3, 0, 0, 2, 0, 4]가 들어왔다고 한다. 
# 그러면 0번 인덱스에 높이 3의 건물이, 
# 3번 인덱스에 높이 2의 건물이, 
# 5번 인덱스에 높이 4의 건물이 있다는 뜻이다. 
# 1번, 2번, 4번 인덱스에는 건물이 없다.
# 사진(폴더 내에 있음)에 따라 총 10만큼의 빗물이 담길 수 있다.
# 그래서 리턴값은 10이다.