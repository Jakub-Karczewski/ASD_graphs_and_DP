from egz2atesty import runtests


class CoalTree:
    
    def __init__(self, n, T):
        self.p = 1

        while self.p < n:
            self.p *= 2
        
        self.t = [T for _ in range(2 * self.p - 1)]

    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2

    def find(self, coal):
        lim = self.p-1
        ind = 0
        
        while ind<lim:
            if self.t[self.left(ind)]>=coal:
                ind = self.left(ind)
            else:
                ind = self.right(ind)

        mag_idx = ind - self.p + 1

        self.t[ind] = self.t[ind] - coal
        ind = self.parent(ind)
        
        while ind >= 0:
            left,right = self.left(ind), self.right[ind]
            max_ = max(self.t[left],self.t[right])
            
            if self.t[ind] == max_:
                break
            
            self.t[ind] = max_
            ind = self.parent(ind)
            
        return mag_idx
    
            
def coal( A, T ):
    n = len(A)

    tree  = CoalTree()
    last = 0
    for transport in A:
        last = CoalTree.find
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
