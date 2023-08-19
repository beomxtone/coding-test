import sys
input = sys.stdin.readline

#
# 1755번: 숫자놀이
# https://www.acmicpc.net/problem/1755
#
# @author  Asher Seo
#


n, m = map(int, input().split())
dict = {}

for num in range(n, m+1):
  res = ''
  for sn in str(num):
    s = int(sn)
    if s == 0:
      res += 'zero '
    elif s == 1:
      res += 'one '
    elif s == 2:
      res += 'two '
    elif s == 3:
      res += 'three '
    elif s == 4:
      res += 'four '
    elif s == 5:
      res += 'five '
    elif s == 6:
      res += 'six '
    elif s == 7:
      res += 'seven '
    elif s == 8:
      res += 'eight '
    elif s == 9:
      res += 'nine '
  dict[res] = num

cnt = 0
for k, v in sorted(dict.items()):
  print(v, end=' ')
  cnt += 1
  if not cnt%10: print()
