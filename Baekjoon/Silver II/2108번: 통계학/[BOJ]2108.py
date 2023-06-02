import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
L.sort()

print(round(sum(L)/n))
print(L[n//2])

third = {}

for num in L:
  if num in third:
    third[num] += 1
  else:
    third[num] = 1

temp = max(third.values())
thirds = []

for i in third:
  if temp == third[i]:
    thirds.append(i)

if len(thirds) > 1:
  print(thirds[1])
else:
  print(thirds[0])

print(L[-1] - L[0])
