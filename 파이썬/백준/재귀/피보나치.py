# 10870 피보나치수 5

n=int(input())

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))
