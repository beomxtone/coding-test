import sys
input = sys.stdin.readline

#
# 2468번: 안전 영역
# https://www.acmicpc.net/problem/2468
#
# 1. 0 ~ max height까지 높이를 모두 BFS 탐색
# 2. BFS 탐색한 결과에 따라 발생한 땅의 수 최대값을 갱신
#
# @author  Asher Seo
#

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(node):
    global cnt
    cnt += 1

    queue = deque()
    queue.append(node)
    copied_graph[node[0]][node[1]] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and copied_graph[nx][ny] != -1:
                copied_graph[nx][ny] = -1
                queue.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
max_height = max(map(max, graph))

for h in range(max_height):
    cnt = 0
    copied_graph = [x[:] for x in graph]
    for i in range(n):
        for j in range(n):
            if copied_graph[i][j] <= h:
                copied_graph[i][j] = -1
    
    for i in range(n):
        for j in range(n):
            if copied_graph[i][j] != -1:
                bfs((i, j))

    ans = max(ans, cnt)

print(ans)
