def main():
    n,h,x = map(int, input().split())
    p = list(map(int, input().split()))
    dic = {j:i+1 for i,j in enumerate(p)}
    ans = float('inf')
    for i in range(n):
        tmp = p[i]
        if tmp+h>=x:
            ans = min(ans, dic[tmp])
    print(ans)

if __name__ == '__main__':
    main()
