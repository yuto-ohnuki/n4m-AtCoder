class UnionFind:
    """
        n : 要素数
        root : 親ノード
        size : グループのサイズ
    """
    
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.size = [1]*(n+1)
    
    """ノードxのrootノードを見つける"""
    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    """木の合併"""
    def Union(self, x, y):
        #入力ノードの親を探索
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        
        #既に同じ木に所属する場合
        if x==y:
            return 
        
        #異なる木に所属する場合 -> sizeが小さい方から大きい方に合併する
        elif self.size[x] > self.size[y]:
            self.size[x] += self.size[y]
            self.root[y] = x
        
        else:
            self.size[y] += self.size[x]
            self.root[x] = y
    
    """xとyが同じグループに所属するか"""
    #　辺(x,y)が橋の場合
    #   ⇒(x,y)以外をUnionしたとき、isSameGroup(self, x, y)=False
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
       
    """ 頂点数を数える"""
    #全連結成分にするために必要な橋の本数は、cnt - 1
    def Count_Vertex(self):
        cnt = 0
        for i in range(self.n):
            if self.root[i+1] < 0:
                cnt += 1
        return cnt
    
    """ xが属する集合に含まれる全ノードを返す """
    def Members(self, x):
        r = self.Find_Root(x)
        return [i for i in range(self.n+1) if self.Find_Root(i) == r]
    
    """xが属する集合のサイズ"""
    def Size(self, x):
        return self.size[self.Find_Root(x)]