import collections
n = int(input())
m = int(input())
T, M  = [[ 0 for _ in range(n)] for _ in range(n)], [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    M[a][b], T[a][b] = c, 1
d = int(input())
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(i == j):
                M[i][j] = 0
            M[i][j] = min(M[i][j], M[i][k] + M[k][j])
print(M)
s, t = 0, n-1
kolej = collections.deque()
#new_graph = [[[] for _ in range(n)] for _ in range(n) ]
vis = [[0 for _ in range(n)] for _ in range(n)]
kolej.append((s, t))
flag = 0
while(len(kolej)):
    x, y = kolej.popleft()
    print(x, y)
    if((x, y) == (t, s)):
        flag = 1
        print("Da sie")
        break
    vis[x][y] = 1
    for i in range(n):
        if(not vis[i][y] and T[x][i] and M[i][y] >= d and M[y][i] >= d):
            kolej.append((i, y))
        if(not vis[x][i] and T[y][i] and M[x][i] >= d and M[i][x] >= d):
            kolej.append((x, i))
if(not flag):
    print("Nie da sie")