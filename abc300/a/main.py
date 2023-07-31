def main():
    n,a,b = map(int, input().split())
    c = list(map(int, input().split()))

    ans = -1
    for i in range(n):
        if c[i] == a+b:
            ans = i
    print(ans+1)

if __name__ == '__main__':
    main()
