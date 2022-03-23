import sys
from collections import deque

test_case = int(sys.stdin.readline())

def bfs(graph, x, y):
    # 상하좌우로 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        # 방문한 곳 0으로 수정
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 벗어나지 않는 조건
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    # 방문한 곳 0으로 수정
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
            else:
                continue

for _ in range(test_case):
    n, m, num = map(int, sys.stdin.readline().split())
    # 다 0인 그래프 생성.
    graph = [[0]*m for _ in range(n)]
    count = 0
    for _ in range(num):
        # 배추 위치는 1로 수정.
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    for a in range(len(graph)):
        while graph[a].count(1) != 0:
            b = graph[a].index(1)
            bfs(graph, a, b)
            count += 1
    print(count)
