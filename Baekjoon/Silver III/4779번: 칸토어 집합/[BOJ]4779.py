import sys
input = sys.stdin.readline

#
# 4779번: 칸토어 집합
# https://www.acmicpc.net/problem/4779
#
# 1. 숫자를 입력받는 재귀함수를 구현한다.
# 2. 입력 값이 0이면 '-'를 리턴한다.
# 3. return cantorSet[n-1] + (' ' * 3**(n-1)) + cantorSet(n-1)
#
# @author  Asher Seo
#

def cantorSet(n):
  if n < 1:
    return '-'
  return cantorSet(n-1) + ' ' * (3**(n-1)) + cantorSet(n-1)

while True:
  try:
    n = int(input())
    print(cantorSet(n))
  except:
    break
  