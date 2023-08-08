import sys
input = sys.stdin.readline

#
# 16926번: 배열 돌리기 1
# https://www.acmicpc.net/problem/16926
#
# 1. 테두리부터 사각형을 하나씩 왼쪽으로 회전
# 2. n과 m 중 작은 값의 절반 만큼 반복하면 된다. (문제의 조건 mod 2 = 0)
# 3. 두 변수의 값을 바꾸는 방법: x, y = y, x
#
# @author  Asher Seo
#

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(r):
  # 행과 열 중 작은 값의 절반 = 회전해야 할 사각형의 수
  repeat = min(n, m) // 2

  for j in range(repeat):
    x, y = j, j
    val = arr[x][y]

    # 왼쪽
    for k in range(x+1, n-j):
      arr[k][j], val = val, arr[k][j]

    # 아래쪽
    for k in range(y+1, m-j):
      arr[n-j-1][k], val = val, arr[n-j-1][k]

    # 오른쪽
    for k in range(n-j-2, j-1, -1):
      arr[k][m-j-1], val = val, arr[k][m-j-1]

    # 위쪽
    for k in range(m-j-2, j-1, -1):
      arr[j][k], val = val, arr[j][k]

for ar in arr:
  print(*ar)
