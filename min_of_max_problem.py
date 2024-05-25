n = int(input())
T = [0] * n
pref = [0] * (n+1)
suma = 0
for i in range(n):
    T[i] = int(input())
    suma += T[i]
    pref[i+1] = suma

print(pref)
X = int(input())
DP = [[[-float('inf') for _ in range(X+1)] for _ in range(n)]  for _ in range(n) ]
def problemitto(i, j, k):
    #print(i, j, k)
    if(k == 0 or j - i + 1 < k):
        return -float('inf')
    if(i == j):
        return T[i]
    if(k == 1):
        return pref[j+1] - pref[i]
    if(DP[i][j][k] != -float('inf')):
        return DP[i][j][k]
    mini = float('inf')
    for x in range(i+1, j):
        for p in range(1, k):
            mini = min(mini, max(problemitto(i, x, p), problemitto(x+1, j, k - p)))
    DP[i][j][k] = mini
    return mini

print(problemitto(0, n-1, X))
