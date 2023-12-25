from collections import deque

"""
Input:
    h,w: length, width of grid
    sy, sx: start point
    gy, gx: goal point
"""
def bfs(h,w,sy,sx,gy,gx,maze):
    visited = [[float('inf')]*w for _ in range(h)]
    visited[sy][sx] = 0
    que = deque([(sy,sx)])
    while que:
        y,x = que.popleft()
        for i,j in ((1,0),(0,1),(-1,0),(0,-1)):
            ny,nx = y+i, x+j
            if 0<=ny<h and 0<=nx<w:
                if (grid[ny][nx]!="#") and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x]+1
                    que.append((ny,nx))
    return visited[gy][gx]

if __name__ == '__main__':
    y,w = map(int, input().split())
    sy,sx = map(int, input().split())
    gy,gx = map(int, input().split())
    grid = [list(map(input())) for _ in range(y)]

    steps = bfs(y,w,sy-1,sx-1,gy-1,gx-1,grid)
    print(steps)