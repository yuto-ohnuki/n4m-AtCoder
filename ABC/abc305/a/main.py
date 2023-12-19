def main():
    n = int(input())
    l = [i*5 for i in range(21)]

    dic = {}

    for i in range(21):
        dif = abs(n - l[i])
        dic[l[i]] = dif
    
    lst = sorted(dic.items(), key=lambda x:x[1])
    print(lst[0][0])


if __name__ == '__main__':
    main()
