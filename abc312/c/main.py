import bisect

def main():
    n,m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    la = len(a)
    lb = len(b)

    if max(b) < min(a):
        print(max(b)+1)
        
    else:
        left = 0
        right = max(max(a), max(b))+1

        while left + 1 < right:
            mid = (left + right) //2

            na = bisect.bisect_right(a, mid)
            nb = lb - bisect.bisect_left(b,mid)

            if na >= nb:
                right = mid
            else:
                left = mid
        
        print(right)

if __name__ == '__main__':
    main()

