def main():
    p,q = input().split()
    cum = [0, 3, 4, 8, 9, 14, 23]
    dic = {}
    char = 'ABCDEFG'
    for i in range(len(char)):
        dic[char[i]] = i
    st = dic[p]
    en = dic[q]
    print(abs(cum[en] - cum[st]))

if __name__ == '__main__':
    main()
