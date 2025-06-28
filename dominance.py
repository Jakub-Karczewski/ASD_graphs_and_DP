from egz2atesty import runtests


def dominance(P):


  class IntervalAdder:
    def __init__(self, n):
      self.p = 1

      while self.p < n:
        self.p *= 2

      self.T = [0 for _ in range(2 * self.p - 1)]

    def parent(self, i):
      return (i - 1) // 2

    def left(self, i):
      return 2 * i + 1

    def right(self, i):
      return 2 * i + 2

    def get(self, i):
      return self.T[i + self.p - 1]

    def set(self, i, val):
      k = i + self.p - 1

      d = val - self.T[k]

      while k >= 0:
        self.T[k] += d

        k = self.parent(k)

    def sum_helper(self, k, lo, hi, i, j):
      if i == lo and j == hi:
        return self.T[k]

      r = (hi - lo) // 2

      if i > lo + r:
        return self.sum_helper(self.right(k), lo + r + 1, hi, i, j)
      elif j <= lo + r:
        return self.sum_helper(self.left(k), lo, lo + r, i, j)
      else:
        res1 = self.sum_helper(self.left(k), lo, lo + r, i, lo + r)
        res2 = self.sum_helper(self.right(k), lo + r + 1, hi, lo + r + 1, j)

        return res1 + res2

    def sum(self, i, j):
      if i > j:
        return 0
      return self.sum_helper(0, self.p - 1, 2 * self.p - 2, i + self.p - 1, j + self.p - 1)

  n = len(P)
  int_add = IntervalAdder(n+1)
  P.sort()
  max_dominating = 0
  count_x = [0 for _ in range(n+1)]
  for x, y in P:
    count_x[x] += 1
  for x, y in P:
    int_add.set(y, int_add.get(y) + 1)
    max_dominating = max(max_dominating, int_add.sum(0, y-1) - (count_x[x] - 1))
  return max_dominating

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
