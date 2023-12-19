from collections import defaultdict

def main():
    n = int(input())
    a = list(map(int, input().split()))

    dic = defaultdict(list)

    for i in range(len(a)):
        dic[a[i]].append(i)
    
    ans = {}
    for k,v in dic.items():
        ans[k] = v[1]
    
    ans = sorted(ans.items(), key=lambda x:x[1])
    
    ans = [x[0] for x in ans]

    print(*ans)

if __name__ == '__main__':
    main()
