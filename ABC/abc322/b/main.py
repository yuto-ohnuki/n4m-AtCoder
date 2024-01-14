def main():
    n,m = map(int, input().split())
    s = input()
    t = input()

    flg1, flg2 = False, False
    if t[:n]==s:
        flg1 = True
    if t[-n:]==s:
        flg2 = True
    
    if flg1 and flg2:
        print(0)
    elif flg1:
        print(1)
    elif flg2:
        print(2)
    else:
        print(3)

if __name__ == '__main__':
    main()
