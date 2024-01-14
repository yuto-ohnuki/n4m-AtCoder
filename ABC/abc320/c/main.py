def main():
    n = input()
    if len(n)==1:
        print("Yes")
    else:
        flg = True
        for i in range(1, len(n)):
            if int(n[i-1]) <= int(n[i]):
                flg = False
        print("Yes" if flg else "No")

if __name__ == '__main__':
    main()
