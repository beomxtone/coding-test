import sys
input = sys.stdin.readline

#
# 9935번: 문자열 폭발
# https://www.acmicpc.net/problem/9935
#
# 1. 폭발문자열을 ''으로 replace -> TLE
# 2. 스택을 활용, 입력 문자열을 하나씩 스택에 넣고 끝 문자열과 폭발 문자열을 비교하여 제거
# 3. 2가 끝나면 최종 결과물 출력, 빈 값이면 'FRULA 출력'
#
# @author  Asher Seo
#

strs = input().rstrip()
boom = input().rstrip()
ans = []

for s in strs:
  ans.append(s)
  
  if len(ans) >= len(boom):
    if boom == ''.join(ans[-1 * len(boom):]):
      for i in range(len(boom)):
        ans.pop()

print(''.join(ans) if len(ans) > 0 else 'FRULA')
