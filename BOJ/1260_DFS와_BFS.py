import sys
from collections import deque
n, m, start = map(int, sys.stdin.readline().split())

# graph 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs, bfs 함수 정의
def dfs(n):
    visited = []
    stack = [n]
    # 작은 정점부터 먼저 방문하기 위해 sort
    global graph
    for i in range(len(graph)):
        graph[i].sort(reverse=True)

    while stack:
        cur_node = stack.pop()
        if cur_node not in visited:
            print(cur_node, end=' ')
            visited.append(cur_node)
            stack.extend(graph[cur_node])

def bfs(n):
    visited = []
    queue = deque([n])

    # 작은 정점부터 먼저 방문하기 위해 sort
    global graph
    for i in range(len(graph)):
        graph[i].sort()

    while queue:
        cur_node = queue.popleft()
        if cur_node not in visited:
            print(cur_node, end=' ')
            visited.append(cur_node)
            queue.extend(graph[cur_node])
    return visited

dfs(start)
print()
bfs(start)


