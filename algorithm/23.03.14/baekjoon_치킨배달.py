import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

def select(i, tmp):
    global result
    if len(tmp) == m:
        result.append(tmp.copy())
        return
    
    if len(tmp):
        result.append(tmp.copy())
    
    for j in range(i, len(chicken)):
        tmp.append(chicken[j])
        select(j+1, tmp)
        tmp.pop()
        
result = []
q = deque([])

def chicken_dist(r):
    visited = [[-1]*n for _ in range(n)]
    dist = 0

    for si, sj in r:
        visited[si][sj] = 0
        q.append((si, sj))
        while q:
            ci, cj = q.pop()
            for d in range(4):
                ni, nj = ci+dx[d], cj+dy[d]
                if 0 <= ni < n and 0 <= nj < n:
                    if arr[ni][nj] == 0 and (visited[ni][nj] == -1 or visited[ni][nj] > visited[ci][cj] + 1):
                        visited[ni][nj] = visited[ci][cj] + 1
                        q.append((ni, nj))
                    elif arr[ni][nj] == 1 and (visited[ni][nj] == -1 or visited[ni][nj] > visited[ci][cj] + 1):
                        visited[ni][nj] = visited[ci][cj] + 1

    for hi, hj in house:
        if visited[hi][hj]:
            dist += visited[hi][hj]
    return dist

select(0, [])
min_dist = 2*n**3

for r in result:
    print(r)
    tmp_dist = chicken_dist(r)
    if tmp_dist < min_dist:
        min_dist = tmp_dist

print(min_dist)
    




