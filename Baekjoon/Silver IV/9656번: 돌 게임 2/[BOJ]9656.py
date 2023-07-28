import sys
input = sys.stdin.readline

#
# 9656번: 돌 게임 2
# https://www.acmicpc.net/problem/9656
#
# 1. n이 홀수이면 창영이가 이긴다.
# 2. n이 짝수이면 상근이가 이긴다.
#
# @author  Asher Seo
#

n = int(input())
print("CY" if n%2 else "SK")
