def main():
    n = int(input())
    a = list(map(int, input().split()))
    src = list(reversed(sorted(a)))
    q, mod = divmod(sum(a), n)
    ans = 0
    for i in range(n):
        if i<mod:
            ans += abs(src[i] - (q+1))
        else:
            ans += abs(src[i] - q)
    print(ans//2)

if __name__ == '__main__':
    main()