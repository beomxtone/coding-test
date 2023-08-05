n = int(input())
cards = set(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

for num in nums:
  print(1 if num in cards else 0, end=" ")