import sys
sys.stdin = open('input.txt')

words = list(input())
for i in range(len(words)):
    if words[i].islower() == True:
        print(words[i].upper(), end='')
    else:
        print(words[i].lower(), end='')
