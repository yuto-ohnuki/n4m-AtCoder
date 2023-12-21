def main():
    n = int(input())
    dic = {}
    for i in range(n):
        c = int(input())
        a = list(map(int, input().split()))
        dic[i] = a
    x = int(input())
    
    ret = []
    mn = float('inf')
    for key, value in dic.items():
        if x in value:
            ret.append((key, len(value)))
            mn = min(mn, len(value))
    
    ans = []
    for i,j in ret:
        if j == mn:
            ans.append(i+1)
    
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()
