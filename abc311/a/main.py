def main():
    n = int(input())
    s = input()

    flg = [False for _ in range(3)]
    ans = -1
    for i in range(n):
        if s[i] == 'A':
            flg[0] = True
        elif s[i] == 'B':
            flg[1] = True
        elif s[i] == 'C':
            flg[2] = True
        
        if sum(flg)==3:
            ans = i
            break
    print(ans+1)


if __name__ == '__main__':
    main()
