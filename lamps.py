from zad3testy import runtests
import copy


def lamps(n, T):
    tree_n = 1
    while n > tree_n:
        tree_n *= 2

    lamps_sum = [[0 for _ in range(3)] for _ in range(2 * tree_n - 1)]
    lazy = [0 for _ in range(2 * tree_n - 1)]
    intervals = [(-1, -1) for _ in range(2 * tree_n - 1)]

    def assign_intervals(ind, L, R):
        intervals[ind] = (L, R)
        lamps_sum[ind][0] = (R - L) + 1
        if L == R:
            return
        assign_intervals(2 * ind + 1, L, (L + R) // 2)
        assign_intervals(2 * ind + 2, (L + R) // 2 + 1, R)

    def update_one_node(ind, L, R, k):
        k = k % 3
        lazy[ind] = (lazy[ind] + k) % 3
        lamps_copy = copy.deepcopy(lamps_sum[ind])
        for i in range(3):
            lamps_sum[ind][(i + k) % 3] = lamps_copy[i]

    def push_down(ind, L, R):
        if lazy[ind] == 0:
            return
        mid = (L + R) // 2

        update_one_node(2 * ind + 1, L, mid, lazy[ind])
        update_one_node(2 * ind + 2, mid + 1, R, lazy[ind])

        lazy[ind] = 0

    def update(ind, L, R, ql, qr):
        if qr < L or ql > R:  # no intersection
            return

        if L >= ql and R <= qr:  # fully contained
            update_one_node(ind, L, R, 1)
            return

        push_down(ind, L, R)

        mid = (L + R) // 2
        if ql <= mid:
            update(2 * ind + 1, L, mid, ql, qr)
        if qr >= mid + 1:
            update(2 * ind + 2, mid + 1, R, ql, qr)

        for i in range(3):
            lamps_sum[ind][i] = lamps_sum[2*ind + 1][i] + lamps_sum[2 * ind + 2][i]

    maxi = 0
    assign_intervals(0, 0, tree_n - 1)
    for (l, r) in T:
        update(0, 0, tree_n - 1, l, r)
        maxi = max(maxi, lamps_sum[0][2])
    return maxi


runtests(lamps)
