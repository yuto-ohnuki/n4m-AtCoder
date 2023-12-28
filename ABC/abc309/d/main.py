from collections import deque

def max_depth(g,root,n):
    que = deque([(root,0)])
    visited = [False for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    while que:
        idx,cnt = que.popleft()
        if visited[idx] is not False:
            continue
        visited[idx] = True
        dist[idx] = min(cnt, dist[idx])
        for nx in g[idx]:
            que.append((nx, cnt+1))
    return dist

def main():
    n1,n2,m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(m)]

    g1 = [[] for _ in range(n1)]
    g2 = [[] for _ in range(n2)]

    for a,b in lst:
        if 1<=a<=n1:
            g1[a-1].append(b-1)
            g1[b-1].append(a-1)
        else:
            g2[a-1-n1].append(b-1-n1)
            g2[b-1-n1].append(a-1-n1)

    d1 = max_depth(g1, 0, n1)
    d2 = max_depth(g2, n2-1, n2)

    print(max(d1)+max(d2)+1)
    

if __name__ == '__main__':
    main()
