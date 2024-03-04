import sys
input = sys.stdin.readline

#
# 1926번: 그림
# https://www.acmicpc.net/problem/1926
#
# 1. BFS 탐색
# 2. 방문 했다면 0으로 변경
#
# @author  Asher Seo
#

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    global count, width
    count += 1
    size = 1

    queue = deque()
    queue.append((start[0], start[1]))
    graph[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                size += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))

    if size > width: width = size


count, width = 0, 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            bfs((i, j))

print(count)
print(width)
