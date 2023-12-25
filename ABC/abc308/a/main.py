def main():
    s = list(map(int, input().split()))
    flg = True
    if s[0]<100 or s[0]>675 or s[0]%25!=0:
        flg = False
    for i in range(1, len(s)):
        pre, cur = s[i-1], s[i]
        if cur < pre:
            flg = False
        if cur<100 or cur>675 or cur%25!=0:
            flg = False
    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()
