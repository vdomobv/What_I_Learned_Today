def sol(place):
    D = [[2, 0], [0, 2], [1, 0], [0, 1], [1, 1], [1, -1]]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for d in range(6):
                    ti, tj = i+D[d][0], j+D[d][1]
                    if ti >= 0 and ti < 5 and tj >= 0 and tj < 5 and place[ti][tj] == "P":
                        if d <= 1:
                            if place[i+D[d+2][0]][j+D[d+2][1]] != "X":
                                return 0
                        elif d == 4:
                            if place[i+D[2][0]][j+D[2][1]] != "X" or place[i+D[3][0]][j+D[3][1]] != "X":
                                return 0
                        elif d== 5:
                            if place[ti][tj+1] != "X" or place[ti-1][tj] != "X":
                                return 0
                        else:
                            return 0
    return 1                           

def solution(places):
    answer = []
    
    for place in places:
        r = sol(place)
        answer.append(r)
    
    return answer