import sys
sys.stdin = open('input.txt')

while True:
    words = input()
    if words == 'END':
        break
    for i in range(len(words) -1, -1, -1):
        print(words[i], end='')
    print()