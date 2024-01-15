""" トポロジカルソート """
"""
  # 閉路がない有向グラフの各有向辺が順方向になるようにソートする手法
  # DAG(有向無閉路グラフ)にのみ適用可能
  # 「トポロジカルソートが可能」と「DAGである」は同値
"""

"""
# 1. BFS 
1. 全ての頂点に対して、入次数をカウント
2. 次数が0の頂点をqueへ追加
3. queの要素数が0になるまでBFS
  3-1. 入次数が0の点を削除
  3-2. 新しく入次数が0になった頂点をqueへ追加
"""
from collections import defaultdict, deque
def TopologicalSort_BFS(v, es):
  # v: node 
  # es: edge list [[u1, v1], [u2, v2] ... ]
  # ins: 入次数

  outs = defaultdict(list)
  ins = defaultdict(int)
  for v1,v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1
  que = deque(v1 for v1 in range(v) if ins[v1]==0)
  ret = []
  while que:
    v1 = que.popleft()
    ret.append(v1)
    for v2 in outs[v1]:
      ins[v2] -= 1
      if ins[v2] == 0:
        que.append(v2)
  return ret

v ,n = map(int, input().split())
es = [list(map(int, input().split())) for _ in range(n)]
lst = TopologicalSort_BFS(v, es)
print(lst)