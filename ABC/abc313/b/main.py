from collections import deque
def main():
    n,m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    ret = [set() for _ in range(n+1)]
    for _ in range(m):
        a,b =  map(int, input().split())
        g[a].append(b)
    for node in range(1, n+1):
        que = deque(g[node])
        while que:
            tmp = que.pop()
            if tmp not in ret[node]:
                ret[node].add(tmp)
                for nx in g[tmp]:
                    que.append(nx)
    ans = -1
    for node in range(1, n+1):
        tmp = list(ret[node])
        if len(tmp) == n-1:
            ans = node
    print(ans)

if __name__ == '__main__':
    main()
