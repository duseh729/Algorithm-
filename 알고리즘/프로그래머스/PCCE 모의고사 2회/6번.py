# 입력 : 5
# 출력 :
# *
# **
# ***
# ****
# *****

# 원래 코드
def solution(n):
	for i in range(n):
		for j in range(i):
			print('*',end='')
		print()

# 고친 코드
def solution(n):
	for i in range(1, n+1):
		for j in range(i):
			print('*',end='')
		print()