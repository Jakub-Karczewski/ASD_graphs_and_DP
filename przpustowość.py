import queue
class Edge:
    def __init__(self, l, r, val):
        self.r = r
        self.l = l
        self.val = val
        self.vis = 0
n = int(input())
m = int(input())
T = [[] for _ in range(n)]
Q = queue.PriorityQueue()
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    kraw = Edge(a, b, c)
    T[a].append(kraw)
wyn = -1
mini = float('inf')
for i in range(len(T[0])):
    val, jd, = T[0][i].val, T[0][i]
    Q.put(((-1)*val, jd))
while(Q.qsize()):
    x, y = Q.get()
    print(y.l, y.r, x)
    if(y.vis):
        continue
    y.vis = 1
    mini = min(mini, (-1)*x)
    beg = y.r
    if(beg == 5):
        break
    for j in range(len(T[beg])):
        if(not T[beg][j].vis):
            Q.put(((-1)* T[beg][j].val, T[beg][j]))
print(mini)