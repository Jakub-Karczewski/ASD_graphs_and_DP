import collections, queue
n = int(input())
m = int(input())
T = [[] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
    T[b].append([a, c])
Q = collections.deque()
short = [-1] * n
vis, dist = [0] * n, [float('inf')] * n
maxi, w = [-1, -1], -1
for k in range(n):
    Q.append(k)
    while(len(Q)):
        w = Q.popleft()
        vis[w] = 1
        for i in range(len(T[w])):
            x = T[w][i][0]
            if(not vis[x]):
                Q.append(x)
    if(maxi[0] == -1):
        maxi[0] = w
    elif(w != maxi[0]):
        maxi[1] = w
    short[k] = w
    for i in range(n):
        vis[i] = 0
print("\nZbior najdalszych:")
print(maxi)
print("\nDla kazdego wierzcholka najbardziej oddalony")
print(short)
kolej = queue.PriorityQueue()
ans = [float('inf'), -1]
for i in range(2):
    for j in range(n):
        vis[j] = 0
        dist[j] = float('inf')
    beg = maxi[i]
    dist[beg] = 0
    kolej.put((0, beg))
    while(kolej.qsize()):
        val, v = kolej.get()
        if(vis[v]):
            continue
        vis[v] = 1
        for k in range(len(T[v])):
            x = T[v][k][0]
            if(not vis[x] and dist[v] + T[v][k][1] < dist[x]):
                dist[x] = dist[v] + T[v][k][1]
                kolej.put((dist[x], x))
    #print(dist)
    for j in range(n):
        if(short[j] == beg):
            if(dist[j] < ans[0]):
                ans = dist[j], j
print()
print(ans)


