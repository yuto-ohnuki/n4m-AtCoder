def main():
    n,m = map(int, input().split())
    lst = []
    for _ in range(n):
        line = list(map(int, input().split()))
        tmp = set(line[2:])
        lst.append([line[0], tmp])

    flg = False
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            pi, fi = lst[i]
            pj, fj = lst[j]
            if pi >= pj and fi <= fj:
                if pi > pj or fj.difference(fi):
                    flg = True
    
    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()
