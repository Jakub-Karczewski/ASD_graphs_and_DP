import math
n = int(input())
m = int(input())
T = [[float('inf') for _ in range(n)] for _ in range(n)]
par, dist = [-1] * n, [float('inf')] * n
for i in range(m):
    a = int(input())
    b = int(input())
    c = float(input())
    T[a][b] = (-1.0) * math.log(2.0, c)
    print(c, T[a][b])
leave = 0
dist[0] = 0
for i in range(n-1):
    flag = 0
    for j in range(n):
        for k in range(n):
            if(dist[j] + T[j][k] < dist[k]):
                flag = 1
                dist[k] = dist[j] + T[j][k]
                par[k] = j
    for j in range(1, n, 1):
        if(dist[j] != float('inf')):
            parent = par[j]
            if(dist[parent] + T[parent][j] < dist[j]):
                leave = 1
                break
    print(dist)
    #print(dist)
    if(leave or not flag):
        break
if(leave):
    print("Detected negative cycle - da sie pomnazac waluty")