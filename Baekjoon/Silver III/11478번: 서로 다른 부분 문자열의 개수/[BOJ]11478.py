s = input()
L = set()

for i in range(len(s)):
  for j in range(len(s)-i):
    subStr = s[i:i+j+1]
    L.add(subStr)
print(len(L))
