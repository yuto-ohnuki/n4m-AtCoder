from itertools import permutations

def main():
    n,m = map(int, input().split())
    g = [[-1]*n for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        g[a-1][b-1] = c
        g[b-1][a-1] = c
    
    ans = 0
    for route in permutations(range(n)):
        tmp = 0
        for i in range(1, n):
            pre, cur = route[i-1], route[i]
            if g[pre][cur] == -1:
                break
            tmp += g[pre][cur]
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()
