import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
bucket = [0 for _ in range(21)]


M = int(input())
for _ in range(M):
    temp = input().rstrip()

    if temp == 'all' or temp == 'empty':
        ins = temp
    else:
        command = temp.split()
        ins = command[0]
        num = int(command[1])
    if ins == 'add':
        bucket[num] = 1
    elif ins == 'remove':
        bucket[num] = 0
    elif ins == 'check':

        if bucket[num] == 1:
            print(1)
        else:
            print(0)
    elif ins == 'toggle':
        if bucket[num] == 1:
            bucket[num] = 0
        else:
            bucket[num] = 1
    elif ins == 'all':
        bucket = [i for i in range(21)]
        pass
    elif ins == 'empty':
        bucket = [0 for _ in range(21)]
