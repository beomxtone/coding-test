import sys
input = sys.stdin.readline
from itertools import product

#
# 7490번: 0 만들기
# https://www.acmicpc.net/problem/7490
#
# 1. itertools의 product를 사용해 +, -, 공백의 연산자들의 중복 순열을 생성
# 2. 각 중복 순열에 대해 식의 결과를 도출, 0이면 True, 0이 아니면 False를 리턴하는 함수 작성
# 3. opr가 공백이면 tmp값과 이어 붙여야하므로, +와 -가 온 경우에 tmp에 저장된 값을 이어 붙인다.
#
# @author  Asher Seo
#

def makeSeq(nums, oprs):
  idx = 1
  tmp = str(nums[0])
  isPstv = True
  res = 0

  for opr in oprs:
    # opr가 공백이면 tmp 값과 이어붙인다
    if opr == ' ':
      tmp += str(nums[idx])
    
    else:
      # opr가 +나 -이면 이전 저장값을 seq에 더하거나 뺀다
      res += int(tmp) if isPstv else -1*int(tmp)

      if opr == '+':
        isPstv = True
      else:
        isPstv = False
      tmp = str(nums[idx])

    idx += 1

  # 맨 마지막 남은 tmp값을 더하거나 뺀다
  if tmp:
    res += int(tmp) if isPstv else -1*int(tmp)

  return True if res == 0 else False


T = int(input())
for _ in range(T):
  N = int(input())
  oprProducts = list(product([' ', '+', '-'], repeat = N-1))

  for oprProduct in oprProducts:
    if makeSeq(range(1, N+1), oprProduct):
      for i in range(N-1):
        print(i+1, end="")
        print(oprProduct[i], end="")
      print(N)
  print()
