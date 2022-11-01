import sys
sys.stdin = open('input.txt')

words = input()

for i in range(1, len(words) + 1):

    print(words[i-1], end='')

    if i % 10 == 0:
        print()
