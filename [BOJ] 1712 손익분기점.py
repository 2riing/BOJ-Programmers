import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
A, B, C = map(int, input().split())# 고정비용, 가변비용, 가격

# 고정비용 // (가격 - 가변비용)
if B >= C:
    print(-1)
else:
    if A % (C -B) >= 0:
        print(A // (C - B) + 1)
    else:
        print(A // (C -B) )

