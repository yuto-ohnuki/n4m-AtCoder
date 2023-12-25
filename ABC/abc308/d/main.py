from collections import deque
def main():
    h,w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    visited = [[False]*w for _ in range(h)]
    
    dict = {cur:nxt for cur,nxt in zip('snuke', 'nukes')}
    idx = (0,0) # y-idx, x-idx
    que = deque([idx])
    if grid[0][0] != 's':
        print("No")
        
    else:
        while que:
            y,x = que.pop()
            c = grid[y][x]
            visited[y][x] = True

            for i,j in ((1,0),(0,1),(-1,0),(0,-1)):
                ny,nx = y+i, x+j
                if 0<=ny<h and 0<=nx<w:
                    if not visited[ny][nx] and grid[ny][nx] == dict[c]:
                        que.append((ny,nx))

        print("Yes" if visited[-1][-1] else "No")

if __name__ == '__main__':
    main()
