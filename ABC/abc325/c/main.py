from collections import deque
def main():
    h,w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    used = [[False]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                used[i][j] = True
            else:
                if used[i][j]:
                    continue
                que = deque([(i,j)])
                cnt += 1

                while que:
                    y,x = que.popleft()
                    used[y][x] = True
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ni, nj = y+di, x+dj
                            if 0<=ni<h and 0<=nj<w:
                                if s[ni][nj]=='#':
                                    if not used[ni][nj]:
                                        que.append((ni, nj))
    
    print(cnt)



if __name__ == '__main__':
    main()
