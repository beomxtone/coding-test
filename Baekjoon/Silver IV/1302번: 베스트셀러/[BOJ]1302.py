import sys
input = sys.stdin.readline

#
# 1302번: 베스트셀러
# https://www.acmicpc.net/problem/1302
#
# @author  Asher Seo
#

n = int(input())
books = {}
for _ in range(n):
  book = input().rstrip()
  if book not in books:
    books[book] = 1
  else:
    books[book] += 1

ans = [k for k, v in books.items() if max(books.values()) == v]
ans.sort()
print(ans[0])
