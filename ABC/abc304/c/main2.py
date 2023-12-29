from collections import deque, defaultdict
def main():
    n,d = map(int, input().split())
    d = d**2
    idx = [list(map(int, input().split())) for _ in range(n)]
    lst = defaultdict(list)
    for i in range(n):
        for j in range(i+1,n):
            tmp = (idx[i][0]-idx[j][0])**2 + (idx[i][1]-idx[j][1])**2
            if tmp <= d:
                lst[i].append(j)
                lst[j].append(i)

    visited = [False]*n
    que = deque([0])
    while que:
        q = que.pop()
        visited[q] = True
        for nx in lst[q]:
            if not visited[nx]:
                que.append(nx)
    
    for ret in visited:
        print("Yes" if ret else "No")

if __name__ == "__main__":
    main()