from collections import defaultdict
def main():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    dic = defaultdict(int)
    for w,x in lst:
        for i in range(x+9, x+18):
            if i > 24:
                i -= 24
            dic[i] += w
        
    print(max(dic.values()))



if __name__ == '__main__':
    main()
