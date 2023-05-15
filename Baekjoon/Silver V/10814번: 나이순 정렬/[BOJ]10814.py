import sys
input = sys.stdin.readline

#
# 10814번: 나이순 정렬
# https://www.acmicpc.net/problem/10814
#
# @author  Asher Seo
#

n = int(input())
L = []
for _ in range(n):
  age, name = input().rstrip().split()
  # age가 str형이면 12, 9 등의 sort가 올바르지 못하므로 int 형변환
  L.append((int(age), name))

L = sorted(L, key = lambda x : x[0])
for i in L: print(i[0], i[1])
