from collections import defaultdict

graph = defaultdict(list)
n, e = map(int, input().split())
s = int(input())
q = []
q.append(s)
size = 0
level = 0
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(max(graph)+1)
visited[s] = True
while q:
    print("LEVEL =", level)
    size = len(q)
    while(size):
        f = q.pop(0)
        print(f)
        for i in graph[f]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
        size = size-1
    level = level+1
