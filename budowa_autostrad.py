n = int(input())
rank, par, c = [0] * n, [i for i in range(n)], [[0, 0] for _ in range(n)]
def dist(a, b):
    return (a[0]-b[0])*(a[0]-b[0]) + (a[1] - b[1]) * (a[1] - b[1])

def Find(ind):
    if(par[ind] == ind):
        return ind
    x = Find(par[ind])
    par[ind] = x
    return x

def Union(a, b):
    a_par = Find(a)
    b_par = Find(b)
    if(rank[a_par] > rank[b_par]):
        par[b_par] = a_par
    else:
        par[a_par] = b_par
        if(rank[a_par] == rank[b_par]):
            rank[b_par] += 1

for i in range(n):
    c[i][0] = int(input())
    c[i][1] = int(input())
edges = []
count, k = 0, 0
for i in range(n):
    for j in range(i+1, n):
        edges.append([dist(c[i], c[j]), i, j])
edges.sort()
print("Posortowane krawedzie")
print(edges, "\n")
res = []
while(k < len(edges) and count < n-1):
    x, y, z = edges[k]
    if(Find(y) != Find(z)):
        Union(y, z)
        res.append([y, z])
        count += 1
    k += 1
if(count == n-1):
    print("Istnieje minimalne drzewo rozpinajace")
    print(x)
    print(res)
    for i in range(len(res)):
        x, y = res[i]
        print("(", c[x][0], ',', c[x][1], ") -> (", c[y][0], ',', c[y][1], ")")