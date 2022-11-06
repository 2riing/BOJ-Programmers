import sys
sys.stdin = open('input.txt')

bucket = [0 for i in range(31)]
for _ in range(28):
    temp = int(input())
    bucket[temp] = 1

for i in range(1, 31):
    if bucket[i] == 0:
        print(i)