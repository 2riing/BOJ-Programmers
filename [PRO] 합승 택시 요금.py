from heapq import heappop, heappush

INF = int(1e9)
graph = [[]]

def preprocess(n, fares):
    global graph
    graph = [[] for i in range(n+1)]
    for fare in fares:
        start, end, cost = fare[0], fare[1], fare[2]
        graph[start].append([end, cost])
        graph[end].append([start, cost])

def dijkstra(start, end):
    global graph
    n = len(graph)
    dist = [INF for i in range(n)]
    dist[start] = 0
    q = [[0, start]] # 거리, 첫정점
    
    while q:
        d, x = heappop(q)
        if dist[x] < d: 
            continue
        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += d
            if ncost < dist[nx]:
                dist[nx] = ncost
                heappush(q, [ncost, nx])
        return dist[end]

def solution(n, s, a, b, fares):
    preprocess(n, fares)
    cost = dijkstra(s, a) + dijkstra(s, b)
    for i in range(1, n + 1):
        if s!= i:
            cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i,b))
    return cost
