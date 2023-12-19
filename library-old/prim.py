def Prim(n,w,cost):
    mincost = [float('inf')]*n
    used = [False]*n
    mincost[0] = 0
    res = 0
    
    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v==-1 or mincost[i] < mincost[v]):
                v = i
        if v == -1:
            break
        used[v] = True
        res += mincost[v]
        for i in range(n):
            mincost[i] = min(mincost[i], cost[v][i])
    return res

def Prim_heap():
    import heapq
    used = [True]*n
    edgelist = []
    for e in edge[0]:
        heapq.heappush(edgelist, e)
    used[0] = False
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, e)
        res += minedge[0]
    return res
n,w = map(int,input().split())
edge = [[] for i in range(n)]
#隣接リスト edge[i]:[コスト,行先]
for i in range(w):
    x,y,z = map(int,input().split())
    edge[x].append([z,y])
    edge[y].append([z,x])
print(Prim_heap())