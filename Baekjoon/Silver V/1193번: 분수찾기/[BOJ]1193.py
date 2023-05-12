import sys
input = sys.stdin.readline

#
# 1193번: 분수찾기
# https://www.acmicpc.net/problem/1193
#
# 1. 대각선을 기준으로 라인의 규칙성을 찾는다.
#    i. line1) 1/1 | line2) 1/2, 2,1 | line3) 3/1, 2/2, 1/3 ...
#   ii. 홀수 라인) x--, y++ / 짝수 라인) x++, y--
# 2. i번째 line에 n이 있다고 할 때, i번째 라인의 몇 번째에 n이 있는지 찾는다.
# 3. 1의 규칙성대로 x와 y의 값을 구해 출력한다.
#
# @author  Asher Seo
#

n = int(input())
line = 0

while n > 0:  # n <= 0 이면 해당 line에 n이 있음
  line += 1
  n -= line
n += line - 1  # index 값을 0부터 표현

if line%2 == 1:  # 홀수 라인
  x = line - n
  y = n + 1
else:  # 짝수 라인
  x = n + 1
  y = line - n
  
print(str(x) + '/' + str(y))