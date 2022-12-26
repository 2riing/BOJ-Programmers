import sys
sys.stdin = open('input.txt')

N = input()
cnt = 0
for i in range(1, int(N) + 1):
    if i < 100:
        cnt += 1
    elif int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
        cnt += 1
print(cnt)
