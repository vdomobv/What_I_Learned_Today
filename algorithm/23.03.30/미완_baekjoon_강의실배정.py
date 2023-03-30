
import sys

n = int(sys.stdin.readline().strip())
cnt = 0

lecture = []
for i in range(n):
    lecture.append(tuple(map(int, sys.stdin.readline().strip().split())))

lecture.sort()

ns, ne = lecture[0][0], lecture[0][1]
for i in range(1, n):
    if ns <= lecture[i][0] < ne or ns < lecture[i][1] <= ne:
        cnt+=1
    
    ns = lecture[i][0]
    ne = lecture[i][1]
    
print(cnt)

# 시간이 겹치는지 확인
    # 시간이 겹치면, 다른 강의실 배정
# 시간이 겹치지 않으면 해당 강의실에 배정

# 내 코드의 문제점 : 한 강의실에 겹치는 지만 확인하고 있다
# 추가된 강의실에서도 겹치는지 안겹치는 지 확인 어떻게 해??
    
"""
    if len(arr) < e:
        t = e-len(arr)+1
    arr.extend([0]*t)
    for j in range(s, e):
        arr[j] += 1
    
print(max(arr))

8
1 8
9 16
3 7
8 10
10 14
5 6
6 11
11 12

답 : 3

"""