import heapq
from collections import defaultdict

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [list(input()) for _ in range(n)]
    cur = {}
    rest = defaultdict(list)
    for e,t in enumerate(s):
        tmp = 0
        for i in range(m):
            if t[i] == 'o':
                tmp += a[i]
            else:
                rest[e].append(-1*a[i])
        cur[e] = tmp + e + 1
        heapq.heapify(rest[e])
    mx = max(cur.values())
    ans = []
    for i in range(n):
        score = cur[i]
        cnt = 0
        while score < mx:
            cnt += 1
            score += heapq.heappop(rest[i])*-1
        ans.append(cnt)
            
    print(*ans, sep='\n')
    


if __name__ == '__main__':
    main()
