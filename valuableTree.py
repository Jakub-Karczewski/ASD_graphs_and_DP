n = int(input())
k = int(input())
G = [[-1, -1, -1, -1] for _ in range(n)]
for i in range(n):
    l = int(input())
    lval = int(input())
    r = int(input())
    rval = int(input())
    G[i] = l, lval, r, rval
print(G)

DP = [[-1 for _ in range(k+1)] for _ in range(n)]

def valuableTree(w, k):
    if(k == 0 or (G[w][0] == -1 and G[w][2] == -1)):
        return 0
    #print(w, k)
    l, lval, r, rval = G[w]
    if(DP[w][k] != -1):
        return DP[w][k]
    if(r == -1):
        return valuableTree(l, k-1) + lval
    if(l == -1):
        return valuableTree(r, k-1) + rval
    maxi = max(lval + valuableTree(l, k-1), rval + valuableTree(r, k-1))
    for x in range(1, k, 1):
        maxi = max(maxi, lval + valuableTree(l, x-1) + rval + valuableTree(r, k-x-1))
    DP[w][k] = maxi
    return maxi
wyn = 0
for i in range(n):
    wyn = max(wyn, valuableTree(i, k))
#print(DP)
print(wyn)
