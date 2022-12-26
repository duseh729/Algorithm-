# year이 4로 나누어 떨어지면 윤년입니다.
# year이 4로 나누어 떨어져도 100으로 나누어 떨어지면 평년입니다.
# year이 100으로 나누어 떨어져도 400으로 나누어 떨어지면 윤년입니다.

def solution(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year%400 == 0:
                return "윤년"
            else:
                return "평년"
        else:
            return "윤년"
    else:
        return "평년"