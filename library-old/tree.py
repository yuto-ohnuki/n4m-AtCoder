'''
  入力
'''
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
  u,v = map(lambda x:int(x)-1, input().split())
  g[u].append(v)
  g[v].append(u)

'''
  0を根とした木に対して、頂点pos以下の頂点数をdfsで求める関数
'''
def search_num_child(pos):
  if num_child[pos]:
    return num_child[pos]
  else:
    num_child[pos] += 1
    for nx in g[pos]:
      if num_child[nx] or nx==pos:
        continue
      num_child[pos] += search_num_child(nx)
    return num_child[pos]
num_child = [0]*n
search_num_child(0)
print(num_child)