# 내가 푼 답
n=int(input())

dic={}
dic['ChongChong']=True
for _ in range(n):
    a, b = input().split()
    if a not in dic:
      dic[a]=False
    if b not in dic:
      dic[b]=False
    if dic[a] or dic[b]:
      dic[a]=True
      dic[b]=True
answer=0
for i in dic:
  if dic[i]:answer+=1
print(answer)

# 제출에 괜찮아 보이는 답
n = int(input())
d = set()
d.add('ChongChong')

for _ in range(n):
    tmp = input().split()
    if tmp[0] in d: d.add(tmp[1])
    elif tmp[1] in d: d.add(tmp[0])
print(len(d))