# n : 頂点数
# w : 辺数

""" グラフを構築する段階 """
n,w = map(int,input().split())     # n:頂点数　, w:辺の数
cost = [[float('inf')]*n for _ in range(n)]
for _ in range(w):    
    x,y,z = map(int,input().split())    # x,y:頂点 , z:辺abのコスト
    cost[x-1][y-1] = z
    cost[y-1][x-1] = z
for i in range(n):
    cost[i][i] = 0     # 自身へのコストは0


# -------------------------------
#   ここから最短経路探索アルゴリズム
# -------------------------------

""" BFS O(M)"""
# 辺のコストがすべて１の場合
def bfs(g):
    print(g)

""" Dijkstra O(MlogN) """
# 辺のコストが非負数の場合の単一始点経路を求める場合
# 頂点sから各頂点への最短距離を探索
def Dijkstra(s,n,w,cost):
    d = [float('inf')]*n
    d[s] = 0
    used = [False]*n
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v==-1):
                v = i
            elif (not used[i]) and d[i]<d[v]:
                v = i
        if v == -1:
            break
        used[v] = True
        for j in range(n):
            d[j] = min(d[j], d[v]+cost[v][j])
    return d

""" Warshall_Floyd O(N^3)"""
# 全点間の距離が必要な場合 (密グラフ)
def Warshall_Floyd(g):
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    return g

""" bellman-ford O(NM) """
# 負のコストがある場合
def Belllman_Ford():
    pass