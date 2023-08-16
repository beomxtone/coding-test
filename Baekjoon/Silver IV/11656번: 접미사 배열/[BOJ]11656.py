import sys
input = sys.stdin.readline

#
# 11656번: 접미사 배열
# https://www.acmicpc.net/problem/11656
#
# @author  Asher Seo
#

str = input().rstrip()
ans = []

for i in range(1, len(str)+1):
  ans.append(str[-i:])

ans.sort()
for an in ans:
  print(an)
