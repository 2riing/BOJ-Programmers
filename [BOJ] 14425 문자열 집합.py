import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
words = []
for _ in range(N):
    temp = input()
    words.append(temp)

wordset = set(words)
cnt = 0
for _ in range(M):
    temp = input()
    if temp in wordset:
        cnt += 1

print(cnt)