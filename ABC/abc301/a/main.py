def main():
    n = int(input())
    s = input()
    a = 0
    for i in range(len(s)):
        if s[i] == 'A':
            a += 1
    t = len(s) - a

    if a!=t:
        print("A" if a>t else "T")
    else:
        aa,tt = 0,0
        for i in range(len(s)):
            if s[i]=='A':
                aa += 1
            else:
                tt += 1
            if aa == a:
                print("A")
                exit()
            elif tt == t:
                print("T")
                exit()

if __name__ == '__main__':
    main()
