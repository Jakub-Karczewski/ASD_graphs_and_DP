n = int(input())
m = int(input())
T = [[] for _ in range(n)]
low, par, vis, czas = [float('inf')] * n, [-1] * n, [0] * n, [-1] * n
for i in range(m):
    a = int(input())
    b = int(input())
    T[a].append(b)
    T[b].append(a)
def DFS(w, time):
    print(w, time)
    vis[w], czas[w] = 1, time
    for i in range(len(T[w])):
        v = T[w][i]
        if(not vis[v]):
            par[v] = w
            DFS(v, time + 1)
    mini = time
    for i in range(len(T[w])):
        v = T[w][i]
        mini = min(mini, low[v])
    parent = par[w]
#Na jutro: krawedz wsteczna musi byc dla roznego od parenta, krawedzie wsteczne sprawdzamy na poczatku najlepiej bo inne wierzcholki
#juz przerobilismy, na koncu po wywolaniu dfsa dla dzieci sprawdzamy jeszcze dla low dzieci
    if(parent != -1):
        mini = min(mini, low[parent])
    low[w] = mini
DFS(0, 1)
print(low)
