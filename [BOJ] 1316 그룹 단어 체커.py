import sys
sys.stdin = open('input.txt')

def Checker(words):
    used = []
    pre = words[0]
    used.append(words[0])
    for i in range(1, len(words)):
        if words[i] not in used:
            used.append(words[i])
        elif words[i] in used and pre != words[i]:
            return False
        pre = words[i]
    return True

N = int(input())
cnt = 0

for _ in range(N):
    words = input()
    if Checker(words):
        cnt += 1

print(cnt)



