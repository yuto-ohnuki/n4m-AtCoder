#迷路に対して、Start->Goalの最短経路コストを返す

"""
入力
　 R : 行数
  C : 列数
  sy,sx : スタート地点座標
  gy,gx : ゴール地点座標
  maze : 迷路 
          ('.' : 道,
           '#' : 壁)
"""

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
maze = [list(input()) for _ in range(R)]

sx,sy = sx-1, sy-1
gx,gy = gx-1, gy-1

def bfs(R,C,sy,sx,gy,gx,maze):
    from collections import deque
    import numpy as np
    INF = np.inf
    visited = [[INF]*C for _ in range(R)]
    visited[sy][sx] = 0
    que = deque([(sy,sx)])
    while que:
        y,x = que.popleft()
        for i,j in ((1,0),(0,1),(-1,0),(0,-1)):
            ny,nx = y+i, x+j
            if 0<=ny<R and 0<=nx<C:
                if (maze[ny][nx]!='#') and visited[ny][nx]==INF:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append((ny,nx))
    return visited[gy][gx]

ans = bfs(R,C,sy,sx,gy,gx,maze)
print(ans)

#Example (ATC002 - A)
"""
<input>
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########

<output>
11
"""