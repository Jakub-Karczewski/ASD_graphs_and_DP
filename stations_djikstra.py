import queue
n = int(input())
m = int(input())
T = [[] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
cost = [0] * n
for i in range(n):
    cost[i] = int(input())
D = int(input())
s = int(input())
t = int(input())
dist = [[float('inf') for _ in range(D+1)] for _ in range(n)]
vis = [[0 for _ in range(D+1)] for _ in range(n)]
dist[s][D] = 0
kolej = queue.PriorityQueue()
kolej.put((0, D, s))
while(kolej.qsize()):
    cash, fuel, nr = kolej.get()
    print(cash, fuel, nr)
    if(vis[nr][fuel]):
        continue
    vis[nr][fuel] = 1
    for i in range(len(T[nr])):
        v, val = T[nr][i]
        if(fuel >= val):
            beg = fuel - val
            for j in range(beg, D+1, 1):
                if(not vis[v][j] and dist[v][j] > cash + (j-beg) * cost[v]):
                    dist[v][j] = cash + (j-beg) * cost[v]
                    kolej.put((dist[v][j], j, v))
print(dist[t])
