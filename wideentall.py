from egz1btesty import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # pole do wykorzystania przez studentow


def wideentall(T):
    depths = [0]

    def dfs_depth(v, d):
        if len(depths) - 1 < d:
            depths.append(1)
        else:
            depths[d] += 1
        if v.left is not None:
            dfs_depth(v.left, d + 1)
        if v.right is not None:
            dfs_depth(v.right, d + 1)

    dfs_depth(T, 0)
    # print(depths)

    best_depth, maxOnLevel = -1, 0
    for i in range(len(depths)):
        if depths[i] >= maxOnLevel:
            best_depth, maxOnLevel = i, depths[i]

    def calculate_to_trim(v, bestDepth, act_depth):
        if v.left is None and v.right is None:
            return 0 if act_depth == bestDepth else -1
        else:
            if act_depth == bestDepth:
                return (v.left is not None) + (v.right is not None)
            else:
                if v.left is not None and v.right is not None:
                    val_left = calculate_to_trim(v.left, bestDepth, act_depth + 1)
                    val_right = calculate_to_trim(v.right, bestDepth, act_depth + 1)
                    if val_left != -1 and val_right != -1:
                        return 0 + val_left + val_right
                    if val_left == -1 and val_right == -1:
                        return -1
                    return val_left + val_right + 2  # Bo jeden z nich jest -1, dlatego dodaje 1
                elif v.left is None:
                    return calculate_to_trim(v.right, bestDepth, act_depth + 1)
                elif v.right is None:
                    return calculate_to_trim(v.left, bestDepth, act_depth + 1)

    return calculate_to_trim(T, best_depth, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=False)
