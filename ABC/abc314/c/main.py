from collections import defaultdict, deque
def main():
    n,m = map(int, input().split())
    s = input()
    c = list(map(int, input().split()))

    dic = defaultdict(list)
    for i in range(n):
        dic[c[i]].append(s[i])
    
    cnt = {key:-1 for key in range(1, m+1)}
    ans = ""
    for i in range(n):
        ans += dic[c[i]][cnt[c[i]]]
        cnt[c[i]] += 1
    print(ans)

if __name__ == '__main__':
    main()