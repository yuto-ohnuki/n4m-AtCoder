def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    for i in range(1, n):
        if a[i] != a[i-1]+1:
            ans = a[i] - 1
            break
    print(ans)

if __name__ == '__main__':
    main()
