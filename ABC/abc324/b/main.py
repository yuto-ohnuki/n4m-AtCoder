def main():
    n = int(input())
    flg = False
    for x in range(70):
        for y in range(40):
            if 2**x * 3**y == n:
                flg = True
    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()
