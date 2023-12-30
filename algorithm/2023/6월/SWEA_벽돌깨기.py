t = int(input())

# n : 타격 횟수
# w : 가로, h : 세로

"""
풀이 접근
1. w 중에 어느 곳을 타격할지 정한다 (for i in range(w): 타격)
2. 한 곳을 타격했을 때, 벽돌이 있으면 깬 벽돌 개수를 추가하고
    해당 벽돌의 수만큼 상하좌우 벽돌을 깬다.
    2-1. 상하좌우의 벽돌들도 깨질 때, 각 벽돌의 수만큼 상하좌우로 깨져야 함.
    2-2. 깨진 벽돌들은 0으로 바꾸고 타격횟가 남았으면 계속 진행한다.
3. 2까지 진행한 후, 다음 타격 위치를 정하는 곳을 0부터 w-1까지 중에서 정한다.
4. 3까지 진행한 후, 타격횟수가 0이 되면 결과를 비교해서 갱신(백트래킹)
"""

for tc in range(1, t+1):
    n, w, h = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(h)]
    total = 0

    for i in range(w):
        cnt = 0
        while n:
            n -= 1
            # for j in range(h)
