def main():
    n,m = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    ans = []

    for i in range(n):
        for j in range(m):

            if i+9>n or j+9>m:
                continue

            flg = True
            for k in range(9):
                fst_line = ''.join(s[i+k][j:j+4]) 
                end_line = ''.join(s[i+k][j+5:j+9])

                if k==0 or k==1 or k==2:
                    if fst_line != '###.':
                        flg = False

                if k==3:
                    if fst_line != '....':
                        flg = False

                if k==5:
                    if end_line != '....':
                        flg = False
                
                if k==6 or k==7 or k==8:
                    if end_line != '.###':
                        flg = False
            
            if flg:
                ans.append([i+1, j+1])
                
    for x in ans:
        print(*x)


if __name__ == '__main__':
    main()

