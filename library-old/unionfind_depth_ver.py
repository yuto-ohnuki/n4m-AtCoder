class UnionFind_VerDepth():
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(0, n+1)]
        self.rank = [1]*(n+1)
    
    """ ノードxの親を探索 """
    def Find_Root(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.Find_Root(self.par[x])
            return self.par[x]
    
    """ 木の合併 """
    def Union(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x==y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    """xとyが同じグループに所属するか"""
    #　辺(x,y)が橋の場合 : isSameGroup(self, x, y)=False
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    
    """ノードxが属する木のサイズ"""
    def Count(self, x):
        return -self.rank[self.Find_Root(x)]     
    
    """木(非連結成分)の数を数える"""
    #全連結成分にするために必要な橋の本数は、cnt - 1
    def Count_Unconnected_Component(self):
        cnt = 0
        for i in range(self.n):
            if self.par[i+1] < 0:
                cnt += 1
        return cnt
    
    def Members(self, x):
        r = self.Find_Root(x)
        return [i for i in range(self.n+1) if self.Find_Root(i) == r]
    
    """xが属する集合の個数"""
    def Size(self, x):
        return -self.par[self.Find_Root(x)]
uf = UnionFind_VerDepth(5)
print(uf.rank)

uf.Union(1,2)
uf.Union(2,3)
uf.Union(4,5)

print(uf.rank)
print(uf.Count_Unconnected_Component())