def main():
    n = int(input())

    if n<=10**3-1:
        print(n)
    else:
        i = 3
        mn = 10**i
        mx = 10**(i+1)-1
        while True:
            if mn<=n<=mx:
                rm = 10**(i-2)
                x = int(n/(rm)) * rm
                print(x)
                break
            else:
                i += 1
                mn = 10**i
                mx = 10**(i+1)-1
        


if __name__ == '__main__':
    main()
