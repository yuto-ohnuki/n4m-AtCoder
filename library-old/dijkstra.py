def dijkstra_heap(s):
    import heapq
    d = [float('inf')]*n
    used = [False]*n
    d[s] = 0
    used[s] = True
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist, e)
    while edgelist:
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in edge[v]:
            if not used[e[1]]:
                heapq.heappush(edgelist, [e[0]+d[v], e[1]])
    return d

n,w = map(int,input().split())
edge = [[] for _ in range(n)]
for i in range(w):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1])
    edge[y-1].append([z,x-1])
print(dijkstra_heap(0))