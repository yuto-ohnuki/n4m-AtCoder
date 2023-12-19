def main():
    n,d = map(int, input().split())
    s = [input() for _ in range(n)]

    ok = [False for _ in range(d)]
    for i in range(d):
        tmp = True
        for j in range(n):
            if s[j][i] == 'x':
                tmp = False
        if tmp:
            ok[i] = True
    
    ans = -1
    tmp = 0
    for x in ok:
        if x:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    else:
        ans = max(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()
