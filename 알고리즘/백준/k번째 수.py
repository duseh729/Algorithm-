# 11004

import sys
input = sys.stdin.readline

a,b=map(int, input().split())

k=list(map(int, input().split()))

print(sorted(k)[b-1])
