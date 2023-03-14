import sys

l, c = map(int, sys.stdin.readline().strip().split())
arr = sys.stdin.readline().strip().split()
# 중복 없음.

# 최소 한개의 모음, 최소 두개의 자음
# 증가하는 순서로 배열
# 가능성 있는 암호들을 다 구한다.

vowel = []
for i in arr:
    if i in ('a','e','i','o','u'):
        vowel.append(i)
        arr.remove(i)

v = c-2 if len(vowel) > c-2 else len(vowel)

def solve(i, e, tmp, arr):
    global result
    if len(tmp) == e:
        result.append(tmp.copy())
        return

    for j in range(i, len(arr)):
        tmp.append(arr[j])
        solve(j+1, e, tmp, arr)
        tmp.pop()

result = []
for e in range(1, v+1):
    solve(0, e, [], vowel)

    for r in result:
        solve
print(ans)