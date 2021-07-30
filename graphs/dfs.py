from collections import defaultdict
graph = defaultdict(list)
q = []


def DFS(s):
    print(s, " ", end='')
    visited[s] = True

    for i in graph[s]:
        if visited[i] == False:
            return DFS(i)


# if __name__ == "__main__":
n, e = map(int, input().split())
s = int(input())
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False]*(max(graph)+1)
k = DFS(s)
