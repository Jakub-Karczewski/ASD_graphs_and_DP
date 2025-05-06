from kol2testy import runtests
import collections


def warrior(G, s, t):
    n = 0
    if s == t:
        return 0
    for i in range(len(G)):
        n = max(n, max(G[i][0], G[i][1]))
    n += 1
    L = [[] for _ in range(n)]
    for (u, v, w) in G:
        L[u].append([v, w])
        L[v].append([u, w])
    Q = collections.deque()
    vis = [[0 for _ in range(17)] for _ in range(n)]
    for i in range(17):
        vis[s][i] = 1
    for v, weight in L[s]:
        if weight <= 16:
            Q.append((v, 16 - weight, weight - 1, 1))
    while len(Q):
        v, remain, weight, dist = Q.popleft()
        if vis[v][remain]:
            continue
        if weight == 0:
            if v == t:
                return dist
            vis[v][remain] = 1
            for neigh, w1 in L[v]:
                if remain - w1 >= 0 and not vis[neigh][remain - w1]:
                    Q.append((neigh, remain - w1, w1 - 1, dist + 1))
            if not vis[v][16]:
                Q.append((v, 16, 8 - 1, dist + 1))
        else:
            Q.append((v, remain, weight-1, dist+1))

    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
