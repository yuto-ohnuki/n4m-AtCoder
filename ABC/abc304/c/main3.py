from collections import deque

def main():
    n,d = map(int, input().split())
    idx = [list(map(int, input().split())) for _ in range(n)]

    res = [False]*n
    res[0] = True
    que = deque([0])

    d = d**2

    while que:
        q = que.popleft()
        for nx in range(n):
            if res[nx]:
                continue
            tmp = (idx[nx][0]-idx[q][0])**2 + (idx[nx][1]-idx[q][1])**2
            if tmp <= d:
                res[nx] = True
                que.append(nx)
    
    for r in res:
        print("Yes" if r else "No")


if __name__ == "__main__":
    main()