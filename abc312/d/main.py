def main():
    s = input()
    MOD = 998244353
    L = len(s)
    if L%2!=0:
        print(0)
    else:
        dp =  [[0]*3010 for _ in range(L+10)]
        dp[0][0] = 1

        for i in range(L):
            c = s[i]

            for j in range(3000):
                if c == '(':
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= MOD
                
                elif c == ')':
                    if i+1 > 2*j:
                        dp[i+1][j] = 0
                    else:
                        dp[i+1][j] += dp[i][j]
                        dp[i+1][j] %= MOD

                else:
                    # '?' --> '('
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= MOD

                    # '?' --> ')'
                    if i+1 > 2*j:
                        dp[i+1][j] = 0
                    else:
                        dp[i+1][j] += dp[i][j]
                        dp[i+1][j] %= MOD
                    
        print(dp[L][L//2]%MOD)

if __name__ == '__main__':
    main()