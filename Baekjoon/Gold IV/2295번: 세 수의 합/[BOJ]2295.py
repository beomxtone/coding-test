import sys
input = sys.stdin.readline

#
# 2295번: 세 수의 합
# https://www.acmicpc.net/problem/2295
#
# 1. x + y + z = k  =>  x + y = k - z 로 바꾼다.
# 2. x + y 의 값을 가진 집합을 생성한다.
# 3. k - z 가 2의 집합에 있는지 확인한다.
#
# @author  Asher Seo
#

n = int(input())
nums = [int(input()) for _ in range(n)]

sets = set()
for x in nums:
    for y in nums:
        sets.add(x + y)

nums = sorted(nums, reverse=True)
for num in nums:
    for z in nums:
        if num - z in sets:
            print(num)
            sys.exit()
