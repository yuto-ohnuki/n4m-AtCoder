## 有向グラフのオイラー回路
## ABC213 D
## dfsによる頂点探索

n = int(input())
v = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int, input().split())
  v[a].append(b)
  v[b].append(a)

ans = []
for x in v:
  x.sort()

def dfs(crr, pre):
  ans.append(crr)
  for nx in v[crr]:
    if nx!=pre:
      dfs(nx, crr)
      ans.append(crr)

dfs(1, -1)
print(*ans)