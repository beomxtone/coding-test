#
# 1026번: 보물
# https://www.acmicpc.net/problem/1026
#
# 1. A[0] * B[0] + ... + A[n-1] * B[n-1] 을 최소값으로 만든다.
# 2. 위의 최소값은 A가 최대일 때, B를 최소로 고르면 된다.
# 3. A는 정렬, B는 역정렬 후 모두 더한 값을 출력한다.
#
# @author  Asher Seo
#

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

ans = 0
for i in range(n):
  ans += A[i] * B[i]

print(ans)
