import queue
n = int(input())
m = int(input())
T = [[] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
    T[b].append([a, c])
Q = queue.PriorityQueue()
min_cycle = float('inf')
vis, dist = [0] * n, [float('inf')] * n
for w in range(n):
    for j in range(len(T[w])):
        v, val = T[w][j]
        for k in range(len(T[w])):
            if(T[w][k][0] != v):
                Q.put((T[w][k][1], T[w][k][0]))
                dist[T[w][k][0]] = T[w][k][1]
        vis[w], dist[w] = 1, 0
        while(Q.qsize()):
            x, hill = Q.get()
            #print(x, hill)
            if(vis[hill]):
                continue
            vis[hill] = 1
            for m in range(len(T[hill])):
                ver, dl = T[hill][m]
                if(not vis[ver] and dist[hill] + dl < dist[ver]):
                    dist[ver] = dist[hill] + dl
                    Q.put((dist[ver], ver))
        min_cycle = min(min_cycle, dist[v] + val)
        #print(min_cycle)
        for k in range(n):
            dist[k] = float('inf')
            vis[k] = 0
print(min_cycle)

