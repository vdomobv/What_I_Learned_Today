t = int(input())

for tc in range(t):
    num = sorted(list(map(int, list(input()))))
    print(num)
    run = 0
    triplet = 0

    for i in set(num):
        if num.count(i) == 3:
            triplet += 1

    tmp = 1
    for i in range(2):      
        if num[i] + 1 == num[i+1]:
            tmp += 1
            if tmp == 3:
                run += 1
        else:
            break
    
    tmp = 1
    for i in range(3, 5):
        if num[i] + 1 == num[i+1]:
            tmp += 1
            if tmp == 3:
                run += 1
        else:
            break
    
    if triplet >= 2 or run >= 2 or (triplet and run):
        print(True)
        # print(triplet, run)
    else:
        print(False)
        # print(triplet, run)


    