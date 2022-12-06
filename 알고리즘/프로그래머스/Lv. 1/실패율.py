#  N	stages	                    result
#  5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
#  4	[4,4,4,4,4]              	[4,1,2,3]

def solution(N, stages):
    answer=[0]*N
    #스테이지별 도달 유저 
    for i in stages:
        if i>N:continue
        else:answer[i-1]+=1
    #실패율 구하기
    n=len(stages)
    k={}
    for j,i in enumerate(answer):
        if i==0:k[j+1]=0
        else:
            k[j+1]=(i/n)
            n-=i
    #실패율 내림차순 정렬
    sorted_k = sorted(k.items(), key=lambda x: x[1], reverse=True)
    m=[]
    for i in sorted_k:
        m.append(i[0])
    return m