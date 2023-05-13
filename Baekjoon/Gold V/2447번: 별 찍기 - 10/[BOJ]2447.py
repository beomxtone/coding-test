import sys
input = sys.stdin.readline

#
# 2447번: 별 찍기 - 10
# https://www.acmicpc.net/problem/2447
#
# @author  Asher Seo
#

def recursive(n):
  if n == 1:
    return '*'
  stars = recursive(n//3)
  arr = []

  for star in stars:
    arr.append(star * 3)
  for star in stars:
    arr.append(star + ' ' * (n//3) + star)
  for star in stars:
    arr.append(star * 3)
  return arr

L = recursive(int(input()))
for line in L:
  print(line)