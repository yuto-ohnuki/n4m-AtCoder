from collections import defaultdict
def main():
    n = int(input())
    s = [list(input()) for _ in range(n)]
    ret = dict()
    cnt = defaultdict(list)
    for i in range(len(s)):
        c = s[i].count('o')
        ret[i] = c
        cnt[c].append(i+1)
    ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)

    used = set([])
    ans = []
    for i,c in ret:
        if c not in used:
            cand = sorted(cnt[c])
            ans += cand
            used.add(c)
    print(*ans)

if __name__ == '__main__':
    main()
