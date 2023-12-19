from collections import deque

# 頂点数N、始点の頂点番号s
N, s = map(int, input().split())
# 隣接リスト。
# edges[i]の要素に(j, c)が含まれる時、iからjにコストcの辺が存在
edges = [[] for i in range(N)]

dist = [10**9]*N
dist[s] = 0
que = deque()
que.append(s)

while len(que) > 0:
    i = que.popleft()
    for j, c in edges[i]:
        d = dist[i] + c
        if d < dist[j]:
            dist[j] = d
            if c == 1:
                que.append(j)
            else:
                que.appendleft(j)