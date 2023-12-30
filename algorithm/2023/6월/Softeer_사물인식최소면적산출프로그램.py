# 각 점들은 총 K개의 색 중 하나
# 각 색을 가지는 점을 하나라도 포함하는 사물 중 가장 작은 것을 찾아서 넓이 산출
# 사물은 직사각형 네변이 모두 수평 혹은 수직
# 경계도 직사각형에 포함

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

lst = [tuple(map(int, input().strip().split())) for _ in range(n)]

sort_x = sorted(lst, key=lambda x: (x[0], x[2]))
sort_y = sorted(lst, key=lambda x: (x[1], x[2]))

area = 4000001
height, width = [[] for _ in range(k)], [[] for _ in range(k)]
check = []
for i in range(n):
    now = sort_x[i]
    for j in range(i+1, n):
        if now[2] != sort_x[j][2]:
            if sort_x[j][2] not in check:
                width = now[0]


print(min(area, area2))

