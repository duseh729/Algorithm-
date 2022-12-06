# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if n<10:return n
    return n%10+sum_digits(n//10)
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 출력:
# 14
# 15
# 16
# 11
# 20

# Basc case: n<10
# 12345일 경우 5.
# 5를 알았으니 1234값의 자릿수 합을 알아햐 한다.