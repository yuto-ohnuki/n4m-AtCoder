def main():
    n = int(input())
    dic = {}
    lst = []
    alst = []
    for _ in range(n):
        s,a = input().split()
        dic[int(a)] = s
        lst.append((s,int(a)))
        alst.append(int(a))
    mn = min(alst)

    lst = lst*2
    for e, (x,y) in enumerate(lst):
        if y==mn:
            for i in range(n):
                print(lst[e+i][0])
            exit()



if __name__ == '__main__':
    main()
