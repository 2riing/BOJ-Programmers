import sys
sys.stdin = open('input.txt')

# 설탕 봉지는 3kg, 5kg, 봉지의 최소개수
N = int(input())

if N % 5 == 0:
    print(N //5)
else:
    cnt = 0
    while N > 0:
        N -=3
        cnt += 1
        if N % 5 == 0:
            print(cnt + (N//5))
            break
        elif N == 1 or N ==2:
            print(-1)
            break
        elif N == 0:
            print(cnt)
            break