def solution(survey, choices):
    answer = ''
    n={'R': 0, 'T':0, 'C':0, 'F':0,'J':0,'M':0,'A':0,'N':0}
    k={1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    #딕셔너리를 이용한 유형별 점수
    for i, j in zip(survey, choices):
        if j<=3:
            n[i[0:1]]+=k[j]
        elif j>=5:
            n[i[1:2]]+=k[j]
    #더 큰 지표 추출(>=를 씀으로써 같은 수는 사전 순 추출)
    answer+='R' if n['R']>=n['T'] else 'T'
    answer+='C' if n['C']>=n['F'] else 'F'
    answer+='J' if n['J']>=n['M'] else 'M'
    answer+='A' if n['A']>=n['N'] else 'N'

    return answer