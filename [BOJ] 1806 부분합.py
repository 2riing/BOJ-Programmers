import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def Check(i):
    global max_length
    temp, cnt = 0, 0
    arr= []
    for j in range(i, N-i+1):
        temp += numbers[j]
        arr.append(numbers[j])
        cnt += 1
        if cnt >= max_length:
            return
        if temp > S and max_length > cnt:
            max_length = cnt
            return

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

max_length = 10000


for i in range(N):
    Check(i)

print(max_length)
