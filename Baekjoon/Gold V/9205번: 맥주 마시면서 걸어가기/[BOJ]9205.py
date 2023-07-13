import sys
input = sys.stdin.readline
from collections import deque

#
# 9205번: 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
#
# 1. [65535][65535] 배열을 생성해서 BFS로 풀이하면 TLE 예상
# 2. 출발점에서 편의점 혹은 목적지에 맥주 20병 안에 도착할 수 있는지 체크한다.
# 3. 어디에도 도착하지 못하면 sad 출력, 목적지에 도착하면 happy를 출력한다.
# 4. 편의점에 도착하면 출발점을 편의점으로 설정, 2부터 반복한다.
#
# @author  Asher Seo
#

def bfs():
  q = deque()
  q.append(start)

  while q:
    x, y = q.popleft()

    if abs(x-end[0]) + abs(y-end[1]) <= 1000:
      print('happy')
      return

    for i in range(n):
      if not visited[i] and abs(x-stores[i][0]) + abs(y-stores[i][1]) <= 1000:
        visited[i] = 1
        q.append((stores[i][0], stores[i][1]))

  print('sad')
  return

t = int(input())
for _ in range(t):
  n = int(input())
  start = tuple(map(int, input().split()))
  stores = [tuple(map(int, input().split())) for _ in range(n)]
  end = tuple(map(int, input().split()))

  visited = [0] * n
  bfs()
