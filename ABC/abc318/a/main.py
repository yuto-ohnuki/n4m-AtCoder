def main():
    n,m,p = map(int, input().split())
    cnt = 0
    while m<=n:
        cnt += 1
        m += p
    print(cnt)

if __name__ == '__main__':
    main()
