import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k=[]
for _ in range(n):
  k.append(input().rstrip())
print(k)
for _ in range(m):
  tmp=input().rstrip()
  if tmp.isdigit():
    print(k[int(tmp)-1])
  else:
    print(k.index(tmp)+1)
