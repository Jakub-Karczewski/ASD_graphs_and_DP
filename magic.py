from egz2btesty import runtests


def magic(C):
    n = len(C)
    maxi = [0 for _ in range(n)]
    available = [False for _ in range(n)]
    available[0] = True
    for i in range(n):
        coin = C[i][0]
        if not available[i]:
            continue
        for j in range(1, 4):
            req, dest = C[i][j]
            if dest >= i and dest != -1:
                if req >= coin:
                    if req - coin <= maxi[i]:
                        available[dest] = True
                        maxi[dest] = max(maxi[dest], maxi[i] - (req-coin))
                else:
                    if coin - req <= 10:
                        available[dest] = True
                        maxi[dest] = max(maxi[dest], maxi[i] + (coin-req))
    print(maxi)
    if not available[-1]:
        return -1
    return maxi[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
