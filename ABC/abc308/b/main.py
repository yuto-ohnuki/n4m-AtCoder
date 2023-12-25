def main():
    n,m = map(int, input().split())
    c = list(input().split())
    d = list(input().split())
    p = list(map(int, input().split()))

    keys = set([])
    ps = dict()

    for x,y in zip(d, p[1:]):
        ps[x] = y
        keys.add(x)

    ans = 0
    for x in c:
        if x in keys:
            ans += ps[x]
        else:
            ans += p[0]

    print(ans)

if __name__ == '__main__':
    main()
