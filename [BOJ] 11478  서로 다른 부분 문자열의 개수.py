from itertools import combinations

words = input()
visited = set()

for i in range(len(words)):
  for j in range(i, len(words)):
    visited.add(words[i : j+ 1])
print(len(visited))
