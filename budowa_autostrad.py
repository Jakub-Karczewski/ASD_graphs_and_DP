n = int(input())
rank, par, c = [[0, 0]] * n, [-1] * n, [0] * n
for i in range(n):
    c[i] = int(input())
c.sort()
count, i = 0
while(count < n-1):
