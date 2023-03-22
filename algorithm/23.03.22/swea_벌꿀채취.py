t = int(input())

for tc in range(1, t+1):
    n, m, c = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(n)]

# 줄을 돌아가면서 가로로 연속되도록 M개의 벌통을 선택
