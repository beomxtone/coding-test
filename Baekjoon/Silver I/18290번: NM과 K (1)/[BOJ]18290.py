import sys
input = sys.stdin.readline

#
# 18290번: NM과 K (1)
# https://www.acmicpc.net/problem/18290
#
# 1. DFS 재귀로 풀이
# 2. (0, 0)부터 시작해서 가능한 경우의 수를 모두 체크
# 3. k개를 뽑았을 때 정답을 갱신
# 4. 마지막까지 검사한 후 정답을 출력
#
# @author  Asher Seo
#

def dfs(x, y, depth, res):
  global ans

  # k개 뽑았으면 정답을 갱신
  if depth == k:
    ans = max(ans, res)
    return

  for i in range(x, n):
    # 현재 보고있는 행이 x와 같으면 y 이후의 열만 봐야하지만, x보다 크면 0부터 본다.
    if i != x: y = 0
      
    for j in range(y, m):
      # 문제의 조건: not checked (x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)
      if (i, j) not in check:
        if (i-1, j) not in check and (i+1, j) not in check and (i, j-1) not in check and (i, j+1) not in check:
          check.append((i, j))
          dfs(i, j, depth+1, res+graph[i][j])
          check.pop()


n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
check = []
ans = -1*(10**9)

dfs(0, 0, 0, 0)
print(ans)
