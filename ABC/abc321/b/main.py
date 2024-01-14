def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    tot = sum(a)
    ans = float('inf')
    for nx in range(101):
        tmp = a + [nx]
        cur = tot + nx - max(tmp) - min(tmp)
        if cur >= x:
            ans = min(ans, nx)
    print(ans if ans!=float('inf') else -1)

if __name__ == '__main__':
    main()
