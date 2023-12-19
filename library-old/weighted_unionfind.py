""" ノード間の距離も管理する場合のUnion-Find木構造 """
class WeightedUnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [-1]*(n+1)
        self.weight = [0]*(n+1)
    
    """ xの根を求める"""
    def Find_Root(self, x):
        if (self.root[x] < 0):
            return x
        else:
            y = self.Find_Root(self.root[x])
            self.weight[x] += self.weight[self.root[x]]
            self.root[x] = y
            return y
    
    """ 木の合併 """
    def Union(self, x, y, w):
        rx = self.Find_Root(x)
        ry = self.Find_Root(y)
        
        if self.rnk[rx] < self.rnk[ry]:
            self.root[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        
        else:
            self.root[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rnk[rx] == self.rnk[ry]:
                self.rnk[rx] += 1
    
    """ xとyが同じ木に所属するかの判定 """
    def IsSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    
    """ x,yのノード重みの取得 """
    def Diff(self, x, y):
        return self.weight[x] - self.weight[y]
    
    """ xが属する木のサイズ(集合の個数)を取得 """
    def Size(self, x):
        return -self.root[self.Find_Root(x)]