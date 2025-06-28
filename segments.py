import random
n = int(input())
beg, end  = [0] * (n+1), [0] * (n+1)
pos = [0] * (n+1)
visr = [0] * (n+1)
beg[0], end[0] = -1, -1
T = [[0, 0] for _ in range(n)]
def binsearch(table, x, flag):
    left, right = -1, len(table)-1
    while(left+1 < right):
        mid = (left+right)//2
        if(table[mid] < x):
            left = mid
        else:
            right = mid
    if(flag):
        return left
    else:
        if(visr[right]):
            visr[right] += 1
            return visr[right] - 1
        else:
            visr[right] = right+1
        return right
def sorted(arr, what):
    def partition(l, r, what):
        if(l >= r):
            return
        x = random.randint(l, r)
        pivot = arr[x] if what else arr[x][0]
        arr[x], arr[r] = arr[r], arr[x]
        j = l
        for i in range(l, r, 1):
            if((what and arr[i] < pivot) or not what and arr[i][0] < pivot):
                arr[i], arr[j], = arr[j], arr[i]
                j += 1
        arr[j], arr[r] = arr[r], arr[j]
        return j

    def quicksort(l, r, what):
        if(l >= r):
            return
        pivot = partition(l, r, what)
        quicksort(l, pivot-1, what)
        quicksort(pivot+1, r, what)
        return
    quicksort(0, len(arr)-1, what)
    return arr

for i in range(n):
    l = int(input())
    r = int(input())
    T[i][0] = l
    T[i][1] = r
    end[i+1] = r
end = sorted(end, 1)
T = sorted(T, 0)
for i in range(n):
    beg[i+1] = T[i][0]
    r = T[i][1]
    pos2 = binsearch(end, r, 0)
    pos[i+1] = pos2

maxi, score = 0, 0
j = 1
l_ext = beg[j]
skip = 1
while(j < n+1):
    left, s = beg[j], 0
    if(left > l_ext):
          l_ext = left
          skip = j
    pos_right = pos[j]
    expand = visr[pos_right] - 1
    started_bef = skip
    s = expand - started_bef
    if(s > maxi):
        maxi = s
    j += 1
print(maxi)
