#Memoization
def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1
        
    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴한다
    if n in cache:
        return cache[n]
    
    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    # 계산한 값을 리턴한다
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)
# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))

#Tabulation
def fib_tab(n):
    # 여기에 코드를 작성하세요
    answer=[0,1,1]
    for i in range(3, n+1):
        answer.append(answer[i-2]+answer[i-1])
    return answer[n]
# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

#공간 최적화
def fib_optimized(n):
    # 여기에 코드를 작성하세요
    current=1
    previous=0

    for _ in range(n-1):
        current, previous=current+previous, current
    return current

# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
