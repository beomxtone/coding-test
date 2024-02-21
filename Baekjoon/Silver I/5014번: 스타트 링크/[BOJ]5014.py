import sys
input = sys.stdin.readline

#
# 5014번: 스타트링크
# https://www.acmicpc.net/problem/5014
#
# 1. 현재 층 S, 목표 층 G, 위 U, 아래 D
# 2. S에서 U와 D씩 이동해서 G로 이동하는 BFS
#
# @author  Asher Seo
#

F, S, G, U, D = map(int, input().split())
flag = False

if S == G:
    print(0)
    sys.exit()

visited = [False] * (F+1)
visited[S] = True

from collections import deque
queue = deque()
queue.append((S, 0))

while queue:
    curr, cnt = queue.popleft()
    up, down = curr + U, curr - D
    if up == G or down == G:
        flag = True
        print(cnt+1)
        break

    if up <= F and not visited[up]:
        visited[up] = True
        queue.append((up, cnt+1))

    if down > 0 and not visited[down]:
        visited[down] = True
        queue.append((down, cnt+1))

if not flag: print('use the stairs')
