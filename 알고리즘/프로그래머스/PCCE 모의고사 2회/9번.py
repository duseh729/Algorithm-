def solution(serial):
    answer = ''
    dic={'10':'operation', '11':'sales', '12':'develop', '13':'finance', 
        '14': 'law', '15':'research'}
    if serial[:2]=='01':
        answer+='male/'
    else:
        answer+='female/'
    answer+=dic[serial[2:4]]+'/'
    answer+=str(int(serial[4:6]))+'team/'
    k=0
    m=serial[0:6]
    for i in m:
        k+=int(i)
    if k%13==int(serial[6:8]):
        answer+='valid'
    else:
        answer+='invalid'
    return answer

# A회사의 사원들에게는 01100103와 같은 일련번호가 주어집니다. 
# 일련번호는 8자리이며 순서대로 두 자리씩 성별, 소속 부서, 소속 팀, 유효성 번호로 구성되어 있습니다.
# 각 정보는 다음과 같다.
# 성별
# male : 01
# female : 02
# 소속 부서
# operation : 10
# sales : 11
# develop : 12
# finance : 13
# law : 14
# research : 15
# 소속 팀
# Nteam : N
# 유효성 번호
# valid: 유효성 번호를 제외한 6개의 숫자들을 모두 더해 13으로 나눈 나머지가 유효성 번호와 같을 때
# invalid: 유효성 번호를 제외한 6개의 숫자들을 모두 더해 13으로 나눈 나머지가 유효성 번호와 다를 때
# 입출력예
# serial	    result
# "01100103"	"male/operation/1team/valid"
# "02131003"	"female/finance/10team/invalid"