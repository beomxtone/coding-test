import sys
input = sys.stdin.readline

#
# 11660번: 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
#
# 1. 2차원 배열의 구간 합 구하는 문제
# 2. 2차원 배열의 누적합을 구한다.
# 3. 2에서 구한 누적합으로 구간합을 구한다.
#
# @author  Asher Seo
#

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 누적합 배열
sumArr = [[0]*(n+1) for _ in range(n+1)]

# 누적합 구하기
for i in range(1, n+1):
  for j in range(1, n+1):
    sumArr[i][j] = arr[i-1][j-1] + sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  # 구간합 구하기
  print(sumArr[x2][y2] - sumArr[x2][y1-1] - sumArr[x1-1][y2] + sumArr[x1-1][y1-1])
