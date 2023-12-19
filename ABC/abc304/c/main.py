from collections import deque, defaultdict
def main():
    n,d = map(int, input().split())
    lst = []
    for _ in range(n):
        x,y = map(int, input().split())
        lst.append((x,y))

    d = d**2
    near = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            xi, yi = lst[i]
            xj, yj = lst[j]
            r = (xi-xj)**2 + (yi-yj)**2
            if r<=d:
                near[i].append(j)
                near[j].append(i)

    que = deque([0])
    flg = [False for _ in range(n)]

    while que:
        ps = que.pop()
        x,y = lst[ps]
        flg[ps] = True
        for nx in near[ps]:
            if not flg[nx]:
                que.append(nx)

    for i in range(n):
        if flg[i]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()