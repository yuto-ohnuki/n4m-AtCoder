def main():
    n,k = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst = sorted(lst, key=lambda x:x[0])
    tot = sum([lst[i][1] for i in range(n)])

    if tot <= k:
        print(1)
    else:
        for a,b in lst:
            tot -= b
            if tot <= k:
                break
        print(a+1)

if __name__ == '__main__':
    main()
