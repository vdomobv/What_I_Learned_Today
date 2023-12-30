import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, list(input().strip()))) for i in range(n)]
visit = [[0]*n for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
o = 1
obstacles = []

def sol(x, y):
  global visit, obstacles, count, o
  
  for k in range(4):
    ni, nj = x + dx[k], y+dy[k]
    if 0 <= ni and ni < n and 0 <= nj and nj < n and arr[ni][nj] == 1 and visit[ni][nj] == 0:
      visit[ni][nj] = 1
      o += 1
      sol(ni, nj)
    

for i in range(n):
  for j in range(n):
    if arr[i][j] != 0 and visit[i][j] == 0 :
      visit[i][j] = 1
      sol(i, j)
      obstacles.append(o)
      o = 1

print(len(obstacles))
obstacles = sorted(obstacles)
for i in obstacles:
  print(i)