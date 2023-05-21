import queue
n = int(input())
m = int(input())
T, M = [[0 for _ in range(n)] for _ in range(n)], [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    M[a][b] = c
stations = int(input())
fuel = [0] * stations
s, t = 0, n-1
for i in range(stations):
    fuel[i] = int(input())
D = int(input())
for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = min(M[i][j], M[i][k] + M[k][j])
Q = queue.PriorityQueue()
Q.put((0, s))
fuel.append(t)
dist, vis = [float('inf')] * (stations+1), [0] * (stations+1)
print(M)
dist[s] = 0
while(Q.qsize()):
    odl, w = Q.get()
    if(vis[w]):
        continue
    if(w == stations):
        break
    vis[w] = 1
    for i in range(stations+1):
        x, v = fuel[w], fuel[i]
        #print(fuel[w], v, M[x][v], dist[w] + M[x][v])
        if(not vis[i] and M[x][v] <= D and dist[w] + M[x][v] < dist[i]):
            dist[i] = dist[w] + M[x][v]
            Q.put((dist[i], i))
print(dist)