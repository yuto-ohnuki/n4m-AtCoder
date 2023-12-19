"""ナップザック問題(重みが小さい場合)  O(nW)"""
def knapsack_1(N, W, w, v):
    #N : 品物数
    #W : 重みの総和
    #lst (wi,vi) : 商品iの重みwi、価値vi
    
    #dp[i+1][j] : i番目までの品物から重さの総和がj以下になるように選んだ場合の価値の総和の最大値
    dp = [[0 for i in range(W+1)] for _ in range(N+1)]
    
    for i in range(N):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i][j - w[i]] + v[i])
    return dp[N][W]


"""ナップザック問題(価値が小さい場合) O(n sigma(V))"""
def knapsack_2(N, W, w, v):
    #dp[i+1][j] : i番目までの品物から価値の総和がjとなるように選んだ場合の重さの総和の最小値
    #             (そのような解が存在しない場合には十分大きな値INFを採用)  
    
    V = sum(v)
    dp = [[float('inf') for i in range(V+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(V+1):
            if j >= v[i]:
                dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])
            else:
                dp[i+1][j] = dp[i][j]
    res = 0
    for j in range(V+1):
        if dp[N][j] <= W:
            res = j
    return res
  
"""個数制限無しナップザック"""


""" LCS(最長共通部分列) """
def LCS(s,t):
    ret = ''
    ls,lt = len(s), len(t)
    
    # dp[i][j] : s_i, t_iでのLCS
    dp = [[0]*(lt+1) for _ in range(ls+1)]
    for i in range(ls):
        for j in range(lt):
            if s[i]==t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    if dp[ls][lt]==0:
        return ret
    i,j = ls, lt
    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            ret += s[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    return ret[::-1]

""" 最長部分増加列 """
def LIS(lst):
  import bisect
  lis = [lst[0]]
  for i in range(len(lst)):
    if lst[i] > lis[-1]:
      lis.append(lst[i])
    else:
      lis[bisect.bisect_left(lis, lst[i])] = lst[i]
  return lis

""" 編集距離 (Lebenshtein Distance) """
# 文字列Aに対して「１文字の追加・削除・置換」の操作により、別の文字列Bへと編集する操作回数
def levenshtein(s1, s2):
    n,m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # 初期化
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    
    # dp
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i-1][j] + 1, # insertion
                dp[i][j-1] + 1, # deletion
                dp[i-1][j-1] + cost # replacement
            )
    
    return dp[n][m]
