n = int(input())
m = int(input())
global czas
czas = 1
T = [[] for _ in range(n)]
time, vis, par = [-1] * n, [0] * n, [-1] * n
deg = [0] * n
sorted = []
for i in range(m):
    a = int(input())
    b = int(input())
    deg[b] += 1
    T[a].append(b)
def DFS(w):
    global czas
    vis[w] = 1
    for i in range(len(T[w])):
        x = T[w][i]
        if(not vis[x]):
            par[x] = w
            DFS(x)
    time[w] = czas
    sorted.append(w)
    czas += 1
root = -1
for i in range(n):
    if(deg[i] == 0):
        root = i
        break
DFS(i)
sorted = sorted[::-1]
#print(sorted)
found = 0
for i in range(n-1):
    x = sorted[i]
    flag = 0
    for j in range(len(T[x])):
        if(T[x][j] == sorted[i+1]):
            flag = 1
            break
    if(not flag):
        found = 1
        print("Nie ma drogi Hamiltona")
if(not found):
    print("Jest droga Hamiltona")
#print(time)
