def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        now = 0
        for j in range(i*7, (i+1)*7):
            now += a[j]
        ans.append(now)
            
    print(*ans)

if __name__ == '__main__':
    main()
