def main():
    n = int(input())
    mat = [[False]*100 for _ in range(100)]

    for _ in range(n):
        a,b,c,d = map(int, input().split())

        for i in range(c,d):
            for j in range(a,b):
                mat[i][j] = True
    
    print(sum([sum(x) for x in mat]))

if __name__ == '__main__':
    main()
