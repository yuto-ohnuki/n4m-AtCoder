def main():
    h,w = map(int, input().split())
    lst = [list(input()) for _ in range(h)]

    xs = set()
    ys = set()
    for i in range(h):
        for j in range(w):
            if lst[i][j] == '#':
                ys.add(i)
                xs.add(j)
    
    mnx, mxx = min(xs), max(xs)
    mny, mxy = min(ys), max(ys)

    for i in range(mny, mxy+1):
        for j in range(mnx, mxx+1):
            if lst[i][j] == '.':
                ans = [i+1, j+1]
                break
    
    print(*ans)



if __name__ == '__main__':
    main()
