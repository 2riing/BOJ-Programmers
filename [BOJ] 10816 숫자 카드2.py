import sys

input = sys.stdin.readline

N = int(input()) # 상근이가 가지고 있는 수자카드의 개수
cards = list(map(int, input().split())) # 숫자 카드 숫자

M = int(input())  # 몇개 가지고 있는지 알아야할  갯수
questions = list(map(int, input().split()))

visited = {}

for i in cards:
  if i in visited:
    visited[i] += 1
  else:
    visited[i] = 1

answer = []

for question in questions:
  if question in visited:
    answer.append(visited[question])
  else:
    answer.append(0)

print(*answer)