import sys
input = sys.stdin.readline

#
# 10972번: 다음 순열
# https://www.acmicpc.net/problem/10972
#
# 1. 원소가 내림차순이면 마지막 순열이므로 -1을 출력하고 종료한다.
# 2. n-1 < n 이면 서로 바꾸고 출력한다.
# 3. n-1 > n 일 때, n-2보다 큰 원소 중 작은 것과 변경한다.
# 4. n-2가 가장 클 경우, n-3 ... n-n 과 비교하고 2, 3의 과정을 반복한다.
#
# @author  Asher Seo
#

def hasHigher(n, arr):
    for elem in arr:
       if elem > n: return True
    return False

def findLower(n, arr):
    for elem in arr:
        if elem > n: return elem
    return None


n = int(input())
perm = list(map(int, input().split()))

# 원소가 내림차순인지 확인
flag = True
for i in range(1, n):
    if perm[i-1] < perm[i]:
        flag = False
        break

# 원소가 내림차순이면 마지막 순열
if flag:
    print(-1)
    sys.exit()

hasAnswer = False

for i in range(n-1, 0, -1):
    if hasAnswer: break

    if perm[i-1] < perm[i]:
        perm[i-1], perm[i] = perm[i], perm[i-1]
        break
  
    for j in range(n-2, -1, -1):
        # j번째 원소와 j뒤의 원소를 비교
        compare_perm = sorted(perm[j+1:])

        if hasHigher(perm[j], compare_perm):
            change_value = findLower(perm[j], compare_perm)
            change_index = perm.index(change_value)
            perm[j], perm[change_index] = perm[change_index], perm[j]

            # 바꾼 원소 뒤의 원소를 오름차순으로 정렬
            after_perm = sorted(perm[j+1:])
            perm = perm[:j+1] + after_perm
            hasAnswer = True
            break

print(*perm)
