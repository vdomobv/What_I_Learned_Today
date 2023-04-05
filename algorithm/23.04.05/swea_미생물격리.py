from collections import deque

t = int(input())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
rd = [0, 1, 0, 3, 2]

for tc in range(1, t+1):
    # 셀의 개수, 격리시간, 군집 개수
    n, m, k = map(int, input().split())
    arr = [[0] * n for _ in range(n)]

    microbe = {}
    # 미생물 군집 입력
    for i in range(1, k+1):
        # [군집 세로위치, 가로위치, 미생물 수, 이동방향]
        t = list(map(int, input().split()))
        microbe[i] = t
        # 현재 위치 표시
        arr[t[0]][t[1]] = i

    # 시간
    time = 0
    while time != m:
        # 군집 반복
        for i in range(1, k):
            # 군집이 있으면
            if microbe.get(i):
                # 현재 군집 정보
                ci, cj, cm, d = microbe.get(i)
                # 이동
                ni, nj = ci + dx[d], cj + dy[d]
                
                # 위치 확인 
                if 0 < ni < n-1 and 0 < nj < n-1:
                    # 이동한 위치에 다른 군집이 있을 경우
                    if arr[ni][nj]:
                        # 이동한 위치에 있는 다른 군집의 정보
                        ti, tj, tm, td = microbe.get(arr[ni][nj])
                        # 방향 변경
                        if tm > cm:
                            d = td
                        # 새로운 정보 갱신
                        microbe[arr[ni][nj]] = [ni, nj, cm+tm, d]
                        # 이전 정보 삭제
                        microbe[i] = 0
                    # 이동한 위치에 다른 군집이 없을 경우
                    else:
                        # 위치 정보 갱신
                        arr[ni][nj] = i

                # 이동한 위치가 가장자리일 경우
                elif ni == 0 or nj == 0 or ni == n-1 or nj == n-1:
                    """
                    약품이 칠해진 가장자리에 이미 다른 군집이 있을때는?
                    """
                    # 군집의 위치 정보 갱신
                    arr[ni][nj] = i
                    # 현재 군집의 위치, 미생물수, 방향 변경
                    microbe[i] = [ni, nj, cm//2, rd[d]] if cm//2 else 0

                # 이전에 있던 위치 정보 삭제 
                arr[ci][cj] = 0
        
        time += 1
    ans = 0
    print(microbe.items())
    for m in microbe.values():
        if m:
            ans += m[2]
    
    print(f"#{tc} {ans}")
