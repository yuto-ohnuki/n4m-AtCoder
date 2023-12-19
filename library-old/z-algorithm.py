""" Z-algorithm """
"""
  # 文字列Sを0文字目からとi文字目から同時に見ていくとき、最大で何文字一致しているか
  # 文字列検索をする際には、SとTを異なる文字'$'等で接続し、S$Tなどとしてから適用
"""

def z_algorithm(s):
  n = len(s)
  ret = [0]*n
  i,j,l = 1,0,n
  ret[0] = n
  while i<l:
    while i+j<l and s[j]==s[i+1]:
      j += 1
    if not j:
      i += 1
      continue
    ret[i] = j
    k = 1
    while l-i>k and k<j-ret[k]:
      ret[i+k] = ret[k]
      k += 1
    i += k
    j -= k
  return ret