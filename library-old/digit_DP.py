""" 桁DP """

# 桁DP : 桁に分けて遷移を考えるDP
# 1~Nまでの整数に対して、「条件を満たす数の総数」「条件を満たす最大値」などを求める
# 
# dp[i][smaller] :=　i桁目まで決定した場合の暫定の値 (smaller : 未満フラグ)
# と定義するのが基本
#
#　遷移は以下が考えらえる
#    ・　dp[i][true]　⇒ dp[i+1][true]にのみ遷移
#    ・ dp[i][false] ⇒ dp[i+1][true]に遷移 (i桁目まではNと等しく、i+1桁目でNより小さい値を選ぶ)
#    ・ dp[i][false] ⇒ dp[i][false]に遷移 (i桁目まではNと等しく、i+1桁目もNと同じ値を選ぶ)
#　( dp[i][true] から dp[i+1][false]の繊維は起きない)

# 桁DPでは繰り上がりの有無に注目すると良い場合も多い
""" 
    例題　：　ABC029 D
    1以上N以下の全ての数において、各桁の「１」の出現回数の総和を数える問題
    (N : 10^9)
"""

n = input()

# dp[i][smaller][j] := i桁目までに1の個数がj個出現する場合の数(smaller:未満フラグ)
dp = [[[0]*11 for _ in range(2)] for _ in range(11)]
dp[0][0][0] = 1

for i in range(len(n)):
    for j in range(10):
        
        """ dp[i][true]⇒dp[i+1][true]の遷移 """
        # smaller=Trueの場合
        # i桁目からi+1桁目の遷移は任意
        dp[i+1][1][j] += dp[i][1][j]*9  # (0, 2~9をi+1桁目として採用)
        dp[i+1][1][j+1] += dp[i][1][j]  # (1をi+1桁目として採用)
        
        """ dp[i][false]⇒dp[i+1][true]の遷移 """
        # smaller==False かつ、i+1桁目はn[i]より小さい場合
        if 1 < int(n[i]):
            # i+1桁目は、0 ~ n[i]-1までの値を採用する場合
            dp[i+1][1][j] += dp[i][0][j]*(int(n[i])-1) # (0~n[i]-1の1以外を採用)
            dp[i+1][1][j+1] += dp[i][0][j]  # (1をi+1桁目として採用)
        elif int(n[i])==1:
            dp[i+1][1][j] += dp[i][0][j] # (i+1桁目に0のみ採用できる)
        
        """ dp[i][false]⇒dp[i+1][false]の遷移 """
        # smaller=False　かつ、i+1桁目もnと同じ文字を採用する場合
        if int(n[i])==1:
            dp[i+1][0][j+1] += dp[i][0][j] # (i+1桁目に1を採用)
        else:
            dp[i+1][0][j] += dp[i][0][j]#(i桁目に1以外を採用)
ans = 0
for i in range(10):
    ans += (dp[len(n)][0][i] + dp[len(n)][1][i])*i
print(ans)