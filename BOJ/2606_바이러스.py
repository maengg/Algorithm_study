import sys
from collections import deque

# 정점의 개수
n = int(sys.stdin.readline())
# 간선 개수
m = int(sys.stdin.readline())

# 그래프 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs 함수 정의
def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        cur_node = queue.popleft()
        if cur_node not in visited:
            visited.append(cur_node)
            queue.extend(graph[cur_node])
    
    return len(visited)

# 1로 인해 감연된 컴퓨터 갯수이기 때문에, 1은 제외 (-1)
print(bfs(1)-1)