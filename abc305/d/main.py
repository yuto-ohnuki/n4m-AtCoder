
import bisect
def main():
    n = int(input())
    a = list(map(int, input().split()))

    cs = [0]
    is_sleep = [False for _ in range(n)]
    for i in range(n):
        if i%2!=0:
            cs.append(cs[-1])
            is_sleep[i] = True
        else:
            if i!=0:
                cs.append(cs[-1]+a[i]-a[i-1])
    
    q = int(input())
    ans = []

    for _ in range(q):
        l,r = map(int, input().split())
        li = bisect.bisect_left(a,l)
        ri = bisect.bisect_left(a,r)

        if not is_sleep[li]:
            x = a[li] - l
        else:
            x = 0

        if not is_sleep[ri]:
            z = r - a[ri-1]
        else:
            z = 0
        y = cs[ri-1] - cs[li]

        ans.append(x+y+z)
    
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
