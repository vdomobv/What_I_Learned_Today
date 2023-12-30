import sys
input = sys.stdin.readline

w, n = map(int, input().split())
metals = [list(map(int,input().split())) for _ in range(n)]

metals = sorted(metals, key = lambda x : -x[1])
result = 0

for weight, price in metals:
  if w > weight:
      result += (weight * price)
      w -= weight
  else:
    result += (w * price)
    break

print(result)