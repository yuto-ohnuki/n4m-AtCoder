def main():
    l = list(map(int, input().split()))
    
    ans = 0
    cur = -1
    for i in range(len(l)):
        if i==0:
            cur = 1
        else:
            cur *= 2

        if l[i]==1:
            ans += cur
    print(ans)

if __name__ == '__main__':
    main()
