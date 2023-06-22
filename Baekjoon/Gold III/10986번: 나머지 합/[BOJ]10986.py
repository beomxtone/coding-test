import sys
input = sys.stdin.readline

#
# 10986번: 나머지 합
# https://www.acmicpc.net/problem/10986
#
# 1. 구간합을 구해서 순회하면 O(n^2)로 TLE
# 2. 0<=A<=B 가 있을 때, [0:A]와 [0:B]의 m으로 나눈 값이 같으면, [A+1:B]도 m으로 나눠떨어진다.
# 3. 2에 따라 m으로 나눠떨어지는 값이 같은 A와 B, 2개를 고르는 경우의 수를 센다.
#
# @author  Asher Seo

n, m = map(int, input().split())
seq = list(map(int, input().split())) + [0]
# 나머지 값을 index, value는 해당 나머지 값의 등장 횟수
cnt = [0]*m

for i in range(n):
  # 구간합 계산
  seq[i] += seq[i-1]
  # cnt의 나머지 값을 +1
  cnt[seq[i] % m] += 1

# 0으로 나눠떨어지는 값
ans = cnt[0]

# x Combination 2 = x(x-1)/2
for x in cnt:
  ans += x*(x-1)//2

print(ans)
