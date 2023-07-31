import sys
input = sys.stdin.readline

#
# 1799번: 비숍
# https://www.acmicpc.net/problem/1799
#
# 1. 브루트포스 = TLE
# 2. 체스 판의 영역을 검은 칸과 흰 칸으로 나누어 풀이
# 3. 시간복잡도는 1/2 * 1/2 해서 1/4만큼 줄어든다.
#
# @author  Asher Seo
#

def dfs(x, y, cnt):
  global res

  # 다음 줄로 0번째, 1번째를 번갈아가며 넘어가기
  if y == n:
    x += 1
    y = 0 if n % 2 else 1
  elif y == n+1:
    x += 1
    y = 1 if n % 2 else 0
  
  # 마지막 줄까지 다 봤을 경우 정답 갱신
  if x == n:
    res = max(res, cnt)
    return

  # 왼쪽 대각선: x-y (+, -), 오른쪽 대각선: x+y (+, +)
  if board[x][y] and not visited[0][x-y] and not visited[1][x+y]:
    visited[0][x-y] = 1
    visited[1][x+y] = 1
    dfs(x, y+2, cnt+1)
    visited[0][x-y] = 0
    visited[1][x+y] = 0

  # 두 칸씩 앞으로
  dfs(x, y+2, cnt)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * (n*2) for _ in range(2)]
res, ans = 0, 0

# 흰색 체스판
dfs(0, 0, 0)
ans += res
res = 0

# 검은색 체스판
dfs(0, 1, 0)
ans += res

print(ans)
