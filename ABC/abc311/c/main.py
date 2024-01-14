def main():
    n = int(input())
    a = [int(x)-1 for x in input().split()]

    lst = [0]
    visited = {0}
    idx = 0

    while True:
        v = a[idx]
        if v in visited:
            u = lst.index(v)
            ans = lst[u:]
            break
        else:
            visited.add(v)
            lst.append(v)
            idx = v
    
    print(len(ans))
    print(*[x+1 for x in ans])

if __name__ == '__main__':
    main()
