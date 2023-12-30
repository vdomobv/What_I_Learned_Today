import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0]
speed = []

for _ in range(n):
  length, limit = map(int, input().split())
  lst.extend([limit]*length)

for _ in range(m):
  l, s = map(int, input().split())
  speed.append([l, s])

result = 0
prev = 0

for i in range(m):
  temp = speed[i][1] - min(lst[prev+1:prev+speed[i][0]+1])
  prev += speed[i][0]
  if temp > result:
    result = temp

print(result)