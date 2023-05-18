n = int(input())
par = [i for i in range(n)]
rank = [0] * n
#print(par)
def Find(x):
    if(x == par[x]):
        return par[x]
    w = Find(par[x])
    par[x] = w
    return w
def Union(x, y):
    x = Find(x)
    y = Find(y)
    if(rank[x] > rank[y]):
        par[y] = x
    else:
        if(rank[x] == rank[y]):
            rank[y] += 1
        par[x] = y
    return
m = int(input())
for i in range(m):
    a = int(input())
    b = int(input())
    Union(a, b)
    Find(a)
    print(par)
