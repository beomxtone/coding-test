import sys
input = sys.stdin.readline

#
# 1181번: 단어 정렬
# https://www.acmicpc.net/problem/1181
#
# @author  Asher Seo
#

n = int(input())
L = []
for _ in range(n):
  word = input().rstrip()
  if word not in L: L.append(word)

L = sorted(L, key = lambda x : (len(x), x))
for i in L: print(i)
