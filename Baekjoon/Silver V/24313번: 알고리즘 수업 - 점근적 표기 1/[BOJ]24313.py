import sys
input = sys.stdin.readline

#
# 24313번: 알고리즘 수업 - 점근적 표기 1
# https://www.acmicpc.net/problem/24313
#
# @author  Asher Seo
#

a, b = map(int, input().split())
c = int(input())
n = int(input())

fn = a * n + b
gn = c * n

print (1 if fn <= gn and c >= a else 0)