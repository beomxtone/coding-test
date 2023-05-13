import sys
input = sys.stdin.readline

#
# 11729번: 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
#
# @author  Asher Seo
#

def hanoi(n, start, end, other):
  if n == 0: return
  hanoi(n-1, start, other, end)
  print(start, end)
  hanoi(n-1, other, end, start)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)