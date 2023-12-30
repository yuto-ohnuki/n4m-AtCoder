def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []

    for i in range(n):
        if i==0:
            ans.append(a[i])
        else:
            cur = a[i]
            pre = a[i-1]

            if cur < pre:
                for x in range(pre-1, cur-1, -1):
                    ans.append(x)
            elif cur > pre:
                for x in range(pre+1, cur+1):
                    ans.append(x)
    print(*ans)

if __name__ == '__main__':
    main()
