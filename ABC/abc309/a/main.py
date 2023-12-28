def main():
    a,b = map(int, input().split())
    lst = []
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(i*3+j+1)
        lst.append(set(tmp))
    
    cur = set([a,b])
    flg = False
    for tmp in lst:
        if cur <= tmp:
            flg = True
    print("Yes" if flg else "No")

if __name__ == '__main__':
    main()
