from collections import Counter
def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = Counter(p)
    mx = max(p)
    if p[0]==mx:
        if cnt[mx]==1:
            print(0)
        else:
            print(1)
    else:
        print(mx-p[0]+1)

if __name__ == '__main__':
    main()
