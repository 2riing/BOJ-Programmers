import sys
sys.stdin = open('input.txt')

total = 0

for i in range(5):
    grade = int(input())
    if grade > 40:
        total += grade
    else:
        total += 40

print(int(total/5))