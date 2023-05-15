import sys
input = sys.stdin.readline

#
# 1427번: 소트인사이드
# https://www.acmicpc.net/problem/1427
#
# @author  Asher Seo
#

n = list(map(int, list(input().rstrip())))
n.sort(reverse=True)
print(''.join(str(x) for x in n))
