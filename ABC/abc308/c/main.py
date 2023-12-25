from decimal import Decimal, getcontext
getcontext().prec = 128

def main():
    n = int(input())

    dict = {}
    for i in range(n):
        a,b = input().split()
        r = Decimal(a) / (Decimal(a) + Decimal(b))
        dict[i+1] = r
    
    ans = list(sorted(dict.items(), key=lambda x:x[1], reverse=True))
    ans = [x[0] for x in ans]
    print(*ans)

if __name__ == '__main__':
    main()
