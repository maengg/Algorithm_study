from collections import deque
n = int(input())
start, end = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [False]*(n+1)

# family에 가족 관계 추가
for _ in range(m):
    p, c = map(int, input().split())
    family[p].append(c)
    family[c].append(p)

def bfs(start, end):
    count = 0
    queue = deque([(start, count)])
    while queue:
        start, count = queue.popleft()
        if start == end:
            return count
        elif not visited[start]:
            # 하나씩 방문할때 마다 +1
            count += 1
            visited[start] = True
            for i in family[start]:
                if not visited[i]:
                    queue.append((i, count))
    return -1

print(bfs(start,end))