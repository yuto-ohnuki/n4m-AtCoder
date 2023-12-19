def fill_grid(g, n, m, pad='0'):
  line = [pad for _ in range(m+2)]
  ret = [line]
  for i in range(n):
    ret.append([pad]+g[i]+[pad])
  ret.append(line)
  return ret

def delete_frame(g):
  ret = []
  for i in range(1, len(g)-1):
    ret.append(g[i][1:-1])
  return ret
