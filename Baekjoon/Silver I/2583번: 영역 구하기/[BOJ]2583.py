import sys
input = sys.stdin.readline

#
# 2583번: 영역 구하기
# https://www.acmicpc.net/problem/2583
#
# 1. 그래프를 1로 초기화 후 사각형 영역을 0으로 변경
# 2. 1인 영역을 bfs 탐색 및 너비 계산
#
# @author  Asher Seo
#

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def fill_square(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 0

def bfs(node):
    global count
    count += 1
    size = 1

    queue = deque()
    queue.append((node))
    graph[node[0]][node[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                size += 1
    return size


count = 0
sizes = []

m, n, k = map(int, input().split())
graph = [[1 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    fill_square(a, b, c, d)

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            sizes.append(bfs((i, j)))

sizes.sort()
print(count)
print(*sizes)
