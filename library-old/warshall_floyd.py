""" warshall_floydによる全点間最短経路探索 0(N^3)"""
def warshall_floyd(g):
  for k in range(len(g)):
    for i in range(len(g)):
      for j in range(len(g)):
        g[i][j] = min(g[i][j], g[i][k]+g[k][j])
  return g

n,w = map(int,input().split())     # n:頂点数　, w:辺の数
g = [[float('inf')]*n for _ in range(n)]
for _ in range(w):    
  x,y,z = map(int,input().split())    # x,y:頂点 , z:辺abのコスト
  g[x-1][y-1] = z
  g[y-1][x-1] = z
for i in range(n):
  g[i][i] = 0     # 自身へのコストは0
print(warshall_floyd(g))
