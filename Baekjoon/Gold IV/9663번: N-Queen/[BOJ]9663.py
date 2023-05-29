import sys
input = sys.stdin.readline

#
# 9663번: N-Queen
# https://www.acmicpc.net/problem/9663
#
# 1. 재귀함수로 퀸을 한 줄에 하나씩 놓는다.
# 2. 퀸을 더 이상 둘 수 없으면 return
# 3. 퀸의 개수가 n개가 되면 count를 1 증가시킨다.
# 4. Python3는 실패, Pypy는 isPossible의 매개변수 차이로 통과
#    매개변수를 더 넣으면 시간이 더 오래 걸리나?
#
# @author  Asher Seo
#

# 퀸을 둘 수 있는지 검사하는 함수
def isPossible(row):
  for i in range(row):
    # row 이전의 행에 같은 열의 값이 있으면 퀸을 둘 수 없다.
    if chess[i] == chess[row]:
      return False
    # 대각선에 다른 퀸이 있으면 퀸을 둘 수 없다.
    if abs(i-row) == abs(chess[i] - chess[row]):
      return False
  
  return True

# 퀸을 두는 경우의 수를 구하는 백트래킹 재귀함수
def setQueen(count):
  if count == n:
    global answer
    answer += 1
    return

  for i in range(n):
    chess[count] = i
    if isPossible(count):
      setQueen(count+1)

# n: 체스판의 크기, 퀸의 개수 (1 ≤ N < 15)
n = int(input())
# chess: n행의 퀸의 위치를 나타내는 배열, chess[i]가 j이면, (i, j)의 위치에 퀸이 있다는 것을 의미
chess = [0]*n
answer = 0

setQueen(0)
print(answer)
