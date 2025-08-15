n = int(input())
T = [[] for _ in range(n)]
for i in range(n - 1):
    a = int(input())
    b = int(input())
    c = int(input())  # weights can be negative
    T[a].append([b, c])
    T[b].append([a, c])
DP = [-1] * n
calc = [0] * n

def good_path(w, prev):
    print(w)
    if DP[w] != -1:
        return DP[w]
    m1, m2 = 0, 0  # We are searching for 2 largest (in terms of weight of single going path) descendants of a vertex
    for i in range(len(T[w])):
        v = T[w][i][0]
        if v != prev:
            res = max(0, T[w][i][1] + max(0, good_path(v, w)))  # max (0, ...) is in case if we do not want to go deeper, because the path weight is negative
            if res > m1:
                m2 = m1
                m1 = res
            elif res > m2:
                m2 = res
    maxi = m1
    DP[w] = maxi  # case if we want to prolong the path "higher" in a tree and end it in a higher subtree
    calc[w] = m1 + m2  # case in which the path ends in this subtree
    return maxi

x = good_path(0, -1)
wyn = 0
for i in range(n):
    wyn = max(wyn, calc[i])
print(calc)
print(wyn)
