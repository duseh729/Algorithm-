# func1(msg) : msg의 글자 수를 세는 함수
# func2(msg) : msg가 숫자로만 이루어져 있는지 확인하는 함수
# func3(msg) : msg에 영어가 존재하는지 확인하는 함수
# func4(msg) : msg에서 공백을 모두 제거하는 함수
# func5(msg) : msg의 3번째, 7번째 자리에 -을 삽입하는 함수
# phone	            result
# "0 10 123 45 678"	"010-1234-5678"
# "010123456789"	    "잘못된 입력입니다"
# "010 a1234 b567"	"잘못된 입력입니다"
# "010 a234 b567"	    "잘못된 입력입니다"

def func1(msg):
    return len(msg)

def func2(msg):
    for letter in msg:
        if '0' <= letter <= '9':
            continue
        return False
    return True

def func3(msg):
    for letter in msg:
        if 'a' <= letter <= 'z':
            return True
        if 'A' <= letter <= 'Z':
            return True
    return False

def func4(msg):
    while(" " in msg):
        msg = msg.replace(" ", "")
    return msg

def func5(msg):
    return msg[:3] + "-" + msg[3:7] + "-" + msg[7:]

# 원래 func만 있었음
def solution(phone):
    phone = func4(phone)

    if not func2(phone) :
        return "잘못된 입력입니다"

    if func1(phone) != 11:
        return "잘못된 입력입니다"

    phone = func5(phone)

    return phone