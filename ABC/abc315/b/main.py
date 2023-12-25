def main():
    m = int(input())
    lst = list(map(int, input().split()))
    mid = (sum(lst)+1)//2
    ans = [-1, 0]
    for i in range(m):
        if ans[1]+lst[i] >= mid:
            ans = [i+1, mid-ans[1]]
            break
        else:
            ans[1] += lst[i]
    print(*ans)

if __name__ == '__main__':
    main()
