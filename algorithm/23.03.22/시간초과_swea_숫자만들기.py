def solve(i):
    global maxV, minV
    if i == n-2:
        tmp = num[0]
        print(' '.join(arr))
        for k in range(n-1):
            if arr[k] == "+":
                tmp += num[k+1]
            elif arr[k] == "-":
                tmp = tmp - num[k+1]
            elif arr[k] == "*":
                tmp *= num[k+1]
            elif arr[k] == "/":
                if num[k+1]*tmp <0:
                    tmp = -(tmp//(-num[k+1]))
                else:
                    tmp = tmp // num[k+1]
        if tmp > maxV:
            maxV = tmp
        if tmp < minV:
            minV = tmp
        return
    
    for j in range(i, n-1):
        arr[i], arr[j] = arr[j], arr[i]
        solve(i+1)
        arr[i], arr[j] = arr[j], arr[i]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))

    op_dict = {0:'+', 1:'-', 2:'*', 3:'/'}
    arr = []

    for i in range(4):
        arr.extend([op_dict[i]]*op[i])
    
    maxV = 0
    minV = 100000000**n
    solve(0)
    print(f"#{tc} {maxV - minV}")
    