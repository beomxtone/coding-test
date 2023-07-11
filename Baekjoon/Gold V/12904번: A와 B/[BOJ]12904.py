import sys
input = sys.stdin.readline

#
# 12904번: A와 B
# https://www.acmicpc.net/problem/12904
#
# 1. 문자열 S를 T로 바꾸는 두 방법을 완전 탐색을 통해 모든 경우의 수 수행 => MLE
# 2. 문자열 T를 맨 뒤 글자에 따라 하나씩 지워가며 S의 길이가 될 때까지 수행
# 3. 최종 결과물이 S와 일치하면 1, 일치하지 않으면 0을 출력
#
# @author  Asher 

S = input().rstrip()
T = list(input().rstrip())

while len(T) > len(S):
  if T.pop() == 'B':
    T = list(reversed(T))

print(1 if ''.join(T) == S else 0)
