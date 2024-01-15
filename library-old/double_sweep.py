""" 木の直径 (最大頂点間距離) を求めるアルゴリズム """
# N : ノード数
# M : 辺数
# G : 木構造をグラフで管理する

from collections import deque
N = int(input())
M = int(input())

# ノード間距離が１の場合を考える
# このとき、接続成分のみを管理すれば十分
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    G[a-1] += [b-1]
    G[b-1] += [a-1]

def bfs(G, s=0):
    que = deque([s])
    dist = [float('inf')]*N
    dist[s] = 0
    while que:
        u = que.popleft()
        for v in G[u]:
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                que += [v]
    return dist

def double_sweep(G):
    dist = bfs(G, s=0)
    ret = -1
    for i in range(N):
        if dist[i] > ret:
            ret = dist[i]
            v = i
    dist = bfs(G, s=v)
    ret = -1
    for i in range(N):
        if dist[i] > ret:
            ret = dist[i]
            w = i
    return v+1, w+1, max(dist)

print(double_sweep(G))