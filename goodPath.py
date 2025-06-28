n = int(input())
T = [[] for _ in range(n)]
for i in range(n-1):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
    T[b].append([a, c])
DP = [-1] * n
calc = [0] * n
def goodpath(w, prev):
    #print(w)
    if(len(T[w]) == 1 and T[w][0][0] == prev):
        return 0
    if(DP[w] != -1):
        return DP[w]
    m1, m2 = 0, 0
    for i in range(len(T[w])):
        v = T[w][i][0]
        if(v != prev):
            res = T[w][i][1] + goodpath(v, w)
            if(res > m1):
                m2 = m1
                m1 = res
            elif(res > m2):
                m2 = res
    maxi = m1
    DP[w] = maxi
    calc[w] = m1 + m2
    #print(w, DP[w], calc[w])
    return maxi
x = goodpath(0, -1)
wyn = 0
for i in range(n):
    wyn = max(wyn, calc[i])
print(calc)
print(wyn)
