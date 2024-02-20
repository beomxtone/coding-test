import sys
input = sys.stdin.readline

#
# 2343번: 기타 레슨
# https://www.acmicpc.net/problem/2343
#
# 1. 구간합 사용 시 합의 중간 점을 찾는 것이 어려움
# 2. 이분 탐색을 활용하여 풀이
# 3. start는 연속된 블루레이 중 가장 작은 값 = 가장 긴 블루레이 하나
# 4. end는 블루레이의 합
#
# @author  Asher Seo
#

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        total, cnt = 0, 1

        for lec in lectures:
            if total + lec > mid:
                cnt += 1
                total = 0
            total += lec

        if cnt <= M:
            res = mid
            end = mid - 1
        else:
            start = mid + 1

    return res
        

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start, end = max(lectures), sum(lectures)
print(binary_search(start, end))
