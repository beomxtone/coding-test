import sys
input = sys.stdin.readline
import math

#
# 2407번: 조합
# https://www.acmicpc.net/problem/2407
#
# @author  Asher Seo
#

n, m = map(int, input().split())
print(math.comb(n, m))
