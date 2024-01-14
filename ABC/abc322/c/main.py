from bisect import bisect_left
def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = set(a)
    ans = []
    for i in range(1, n+1):
        if i in a:
            ans.append(0)
        else:
            nx = bisect_left(a, i)
            ans.append(a[nx] - i)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
