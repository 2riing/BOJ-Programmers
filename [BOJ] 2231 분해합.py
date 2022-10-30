import sys
sys.stdin = open('input.txt')

def hap():
    for i in range(1, 10):
        temp[0] = str(i)
        for j in range(1, 10):
            temp[1] = str(j)
            for k in range(1, 10):
                temp[2] = str(k)
                print(temp)
                if int(''.join(temp)) + int(temp[0]) + int(temp[1]) + int(temp[2]) == N:
                    return int(''.join(temp))

N = int(input())

temp = [0, 0, 0]

answer = hap()
if answer:
    print(answer)
else:
    print(0)
