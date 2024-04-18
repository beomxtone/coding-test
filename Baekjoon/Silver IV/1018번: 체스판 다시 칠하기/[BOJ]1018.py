import sys
input = sys.stdin.readline

#
# 1018번: 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
#
# 1. 맨 왼쪽 위가 W, B인 경우 두 가지가 있다.
# 2. 입력 보드에서 8x8 만큼 자른다.
# 3. 1의 값과 다른 값의 최소값을 출력한다.
#
# @author  Asher Seo
#

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
ans = 10**9

for i in range(n-7):
  for j in range(m-7):
    wCnt, bCnt = 0, 0

    for x in range(i, i+8):
      for y in range(j, j+8):
        if (x + y) % 2 == 0:
          if board[x][y] == 'W': bCnt += 1
          else: wCnt += 1
        else:
          if board[x][y] == 'W': wCnt += 1
          else: bCnt += 1

    ans = min(ans, wCnt, bCnt)

print(ans)
