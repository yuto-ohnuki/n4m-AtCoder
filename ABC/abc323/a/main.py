def main():
    s = input()
    flg = True
    for i in range(len(s)):
        if i%2!=0 and s[i]=='1':
            flg = False
    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()
