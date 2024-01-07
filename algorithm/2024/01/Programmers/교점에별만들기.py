def solution(line):
    x_point = []
    y_point = []
    for i in range(len(line)-1):
        a, b, e = line[i][0], line[i][1], line[i][2]
        for j in range(i+1, len(line)):
            c, d, f = line[j][0], line[j][1], line[j][2]
            t = (a*d) - (b*c)
            if t != 0:
                x = ((b*f) - (e*d))/t
                y = ((e*c) - (a*f))/t
                if float.is_integer(x) and float.is_integer(y):
                    x_point.append(int(x))
                    y_point.append(int(y))
    mxx = max(x_point)
    mix = min(x_point)
    mxy = max(y_point)
    miy = min(y_point)
    
    m = mxx - mix + 1
    n = mxy - miy + 1
    
    result = [["." for _ in range(m)] for _ in range(n)]
    temp = []
    for i in range(len(x_point)):
        tx = abs(x_point[i] - mix)
        ty = abs(y_point[i] - mxy)
        temp.append([tx, ty])

    for i, j in temp:
        result[j][i] = "*"
    
    answer = []
    for i in result:
        answer.append("".join(i))
    
    return answer