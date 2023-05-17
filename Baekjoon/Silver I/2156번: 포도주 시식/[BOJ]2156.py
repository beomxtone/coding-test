import sys
input = sys.stdin.readline

#
# 2156번: 포도주 시식
# https://www.acmicpc.net/problem/2156
#
# 1. 아이디어: d[i] = i번째 까지의 포도주 배열에서 마실 수 있는 최대값
#     i. i-2, i-1번째 포도주를 마신다. (i-1번째까지 포도주를 마신다.)
#    ii. i-2,   i번째 포도주를 마신다. (i-2번째까지 포도주를 마신다.)
#   iii. i-1,   i번째 포도주를 마신다. (i-3번째까지 포도주를 마신다.)
# 2. d[i] = max( d[i-1], d[i-2] + w[i], d[i-3] + w[i-1] + w[i] )
#
# @author  Asher Seo
#

n = int(input())
w = [0]
for _ in range(n):
  w.append(int(input()))

if n == 1:
  print(w[1])
  exit()

d = [0]*(n+1)
d[1] = w[1]
d[2] = w[1] + w[2]

for i in range(3, n+1):
  d[i] = max(
    d[i-1],  # i-1번째 까지 포도주를 마신다.
    d[i-2] + w[i],  # i-2번째 까지 포도주를 마신다.
    d[i-3] + w[i-1] + w[i] )  # i-3번째까지 포도주를 마신다.
print(d[n])
