'''
카드 색 : 8개
카드팩 종류 : N가지

카드 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어 있음
카드 N개 구매

- 1차 실패 반례
p = [0]
p.extend(list(map(int, input().strip().split())))

lst = [0] * (n+1)

for i in range(1, n+1):
    lst[i] = max(p[i]*(n//i)+p[n%i], p[i-1])

    10
    1 100 160 1 1 1 1 1 1 1 
    답 : 520    오답 : 500
==> 작은 수로 해당 수의 일부를 만들 수 있을때를 고려

풀이 접근 방법
0. 값을 저장할 새배열 생성
1. 1부터 n까지 돌면서 카드를 i개 구매할 때, 최대값으로 배열에 저장해준다.
    현재 배열의 값과 j만큼 빼고 j개 팩의 가격을 더한 값을 비교해서 더 큰값을 저장
'''
import sys
input = sys.stdin.readline

n = int(input().strip())
p = [0]
p.extend(list(map(int, input().strip().split())))

lst = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        lst[i] = max(lst[i], lst[i-j] + p[j])

print(lst[n])