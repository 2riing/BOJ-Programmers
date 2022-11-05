import sys
sys.stdin = open('input.txt')

X = int(input()) # 영수증에 적힌 금액
N = int(input()) # 구매한 물건의 종류 수
total = 0
for _ in range(N):
    price, cnt = map(int, input().split())
    total += (price * cnt)

if (total == X):
    print('Yes')
else:
    print('No')