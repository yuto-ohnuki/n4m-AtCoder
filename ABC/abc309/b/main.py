def main():
    n = int(input())
    mat = [list(input()) for _ in range(n)]

    ans = [[None]*n for _ in range(n)]
    ans[0][0] = mat[1][0]
    for i in range(n-1):
        ans[0][i+1] = mat[0][i] 
    for i in range(n-1):
        ans[i+1][-1] = mat[i][-1]
    for i in reversed(range(n-1)):
        ans[-1][i] = mat[-1][i+1]
    for i in reversed(range(n-1)):
        ans[i][0] = mat[i+1][0]

    for i in range(n):
        for j in range(n):
            if ans[i][j] == None:
                ans[i][j] = mat[i][j]
    for line in ans:
        print(''.join(line))

if __name__ == '__main__':
    main()
