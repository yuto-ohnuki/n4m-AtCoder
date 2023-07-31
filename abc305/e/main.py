from collections import deque

def main():
    n,m,k = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    
    que = deque([])
    for _ in range(k):
        p,h = map(int, input().split())
        que.append((p-1, h))

    flg = [False for _ in range(n)]
    while que:
        idx,h = que.popleft()
        nq = deque([(idx, 0)])
        nflg = [False for _ in range(n)]
        while nq:
            idx, d = nq.pop()
            nflg[idx] = True
            
            if not flg[idx]:
                flg[idx] = True
            
            for nxt in edge[idx]:
                if flg[idx]:
                    if not nflg[nxt] and d+1<=h:
                        nq.append((nxt, d+1))
    
    print(sum(flg))
    ans = [i+1 for i in range(n) if flg[i]]
    print(*ans)

if __name__ == '__main__':
    main()
