""" bitDP (集合をbitのフラグで管理するDP) """
# dp[S][v] := 頂点0でスタートし、{0,1,2,...,n-1}の部分集合Sを巡回する[S]!通りの経路のうち、最後に頂点vに到達した最短距離
# 更新式：dp[S U {v}][v] = min( dp[S][u] + cost(u,v) )
# 計算量 O(n^2 * 2^n)　(全探索するとO(n!)で膨大)

v,e = map(int, input().split())
g = [[float('inf')]*v for _ in range(v)]
for i in range(e):
    s,t,d = map(int, input().split())
    g[s-1][t-1] = d
dp = [[float('inf')]*v for _ in range(2**v)] # 各bitが2値なので、dp長さは2^v必要
dp[0][0] = 0

for s in range(2**v):
    for i in range(v): # 配られる側
        for j in range(v): # 配る側

            # j番目の頂点に訪れていない、またはどの頂点にも訪れていない場合 
            if not (s>>j)&1 and s!=0:
                continue

            # i番目の頂点に訪れていない場合 (j番目の頂点には訪れている)
            if (s>>i)&1==0:

                # 更新式
                if dp[s][j]+g[j][i] < dp[s|(1<<i)][i]:
                    dp[s|(1<<i)][i] = dp[s][j] + g[j][i]

if dp[2**v-1][0] != float('inf'):
    print(dp[2**v-1][0])
else:
    print(-1)