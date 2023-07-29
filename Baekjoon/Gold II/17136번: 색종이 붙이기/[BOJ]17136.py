import sys
input = sys.stdin.readline

#
# 17136번: 색종이 붙이기
# https://www.acmicpc.net/problem/17136
#
# 1. DFS로 브루트포스 수행
# 2. 같은 크기의 색종이를 5번 넘게 사용하면 break
# 3. Pypy로 제출시 통과, python은 TLE => 개선이 필요
#
# @author  Asher Seo
#

two = [(0, 1), (1, 0), (1, 1)]
three = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
four = [(0, 3), (1, 3), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
five = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

def dfs(x, y, papers):
  global ans

  # 색종이를 5개 이상 사용했는지 검사
  for key in range(1, 6):
    if papers[key] > 5: return

  if ans < sum(papers.values()): return
      
  # 색종이로 덮을 영역이 없으면 정답 갱신
  flag = 1
  for i in range(10):
    if sum(board[i]) != 0:
      flag = 0
      break

  if flag:
    ans = min(ans, sum(papers.values()))
    return

  if x >= 10: return

  if board[x][y]:
    # 색종이로 덮을 수 있는 영역 검사
    isFive, isFour, isThree, isTwo = 1, 1, 1, 1

    for k in range(3):
      dx, dy = x + two[k][0], y + two[k][1]
      if dx > 9 or dy > 9:
        isTwo, isThree, isFour, isFive = 0, 0, 0, 0
        break
      if not board[dx][dy]:
        isTwo, isThree, isFour, isFive = 0, 0, 0, 0
        break

    if isThree:
      for k in range(5):
        dx, dy = x + three[k][0], y + three[k][1]
        if dx > 9 or dy > 9:
          isThree, isFour, isFive = 0, 0, 0
          break
        if not board[dx][dy]:
          isThree, isFour, isFive = 0, 0, 0
          break

    if isFour:
      for k in range(7):
        dx, dy = x + four[k][0], y + four[k][1]
        if dx > 9 or dy > 9:
          isFour, isFive = 0, 0
          break
        if not board[dx][dy]:
          isFour, isFive = 0, 0
          break

    if isFive:
      for k in range(9):
        dx, dy = x + five[k][0], y + five[k][1]
        if dx > 9 or dy > 9:
          isFive = 0
          break
        if not board[dx][dy]:
          isFive = 0
          break

    # 크기 n의 색종이를 덮을 수 있는 경우
    if isFive: coverPaper(papers, 5, x, y)
    if isFour: coverPaper(papers, 4, x, y)
    if isThree: coverPaper(papers, 3, x, y)
    if isTwo: coverPaper(papers, 2, x, y)
    coverPaper(papers, 1, x, y)

  else:
    if y < 9: dfs(x, y+1, papers)
    else:
      if x == 9: return
      else: dfs(x+1, 0, papers)

def coverPaper(papers, n, x, y):
  papers[n] += 1
  
  for i in range(n):
    for j in range(n):
      if x+i < 10 and y+j < 10:
        board[x+i][y+j] = 0

  if y < 9: dfs(x, y+1, papers)
  else: dfs(x+1, 0, papers)
  
  papers[n] -= 1
  for i in range(n):
    for j in range(n):
      if x+i < 10 and y+j < 10:
        board[x+i][y+j] = 1


board = [list(map(int, input().split())) for _ in range(10)]
usedPaper = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
ans = 26

dfs(0, 0, usedPaper)
print(ans if ans < 26 else -1)
