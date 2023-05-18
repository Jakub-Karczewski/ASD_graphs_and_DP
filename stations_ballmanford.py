#from WIET import syndrom_sztokholmski
import collections
def wypisz(T):
    for i in range(len(T)):
        for j in range(len(T[0])):
            print(T[i][j], end = ' ')
        print()

n = int(input())
m = int(input())
T = [[] for _ in range(n)]
def nwd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a

step, maxi = 0, 0

for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
    #T[b].append([a, c])
    step = c if i == 0 else nwd(step, c)
    maxi = max(maxi, c)
cost = [0]*n
vis = [0] * n
#print("Podaj ceny paliwa:")
for i in range(n):
    cost[i] = int(input())
#print("Podaj pojemność")
D = int(input())
#print("podaj s i t")
s = int(input())
t = int(input())
step = nwd(step, D)
x = D//step
DP = [[ float('inf') for _ in range(x+1)] for _ in range(n)]
DP[0][x] = 0
for k in range(n):
    for i in range(n):
        w, v = i, -1
        if(i != t):
            for j in range(len(T[i])):
                v, val = T[i][j]
                delta = val//step
                start = x - delta + 1
                for h in range(start):
                    for m in range(h+1):
                        DP[v][h] = min(DP[v][h], DP[w][m+delta] + (h-m) * cost[v] * step)
                for l in range(x+1):
                    for z in range(l):
                        DP[v][l] = min(DP[v][l], DP[v][z] + (l - z) * cost[v] * step)

print()
wypisz(DP)
print("\nwynik:", DP[t][0])