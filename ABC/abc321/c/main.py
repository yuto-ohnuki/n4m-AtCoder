def main():
    k = int(input())
    n = 5
    dp = [[0 for _ in range(10)] for _ in range(n)]
    for i in range(10):
        if i==0:
            continue
        else:
            dp[1][i] = 1
            dp[2][i] = i
    
    for i in range(3, n):
        tmp = 0
        for j in range(1, 10):
            if j<i-1:
                continue
            tmp += dp[i-1][j-1]
            dp[i][j] = tmp
    
    dig_sum = [sum(line) for line in dp]
    print(dig_sum)

    tmp = 0
    for i in range(10):
        if tmp+dig_sum[i] < k:
            tmp += dig_sum[i]
        else:
            break

if __name__ == '__main__':
    main()
