#!/usr/bin/env python3

def main():
    n = int(input())
    s = input()
    t = input()


    flg = True
    for i in range(n):
        sc = s[i]
        tc = t[i]

        tmp = False
        if sc==tc:
            tmp = True
        if (sc=='1' and tc=='l') or (sc=='l' and tc=='1'):
            tmp = True
        if (sc=='0' and tc=='o') or (sc=='o' and tc=='0'):
            tmp = True
        
        if not tmp:
            flg = False

    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()