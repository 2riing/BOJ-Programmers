import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split()) # 현재 시간, 분
C = int(input()) # 필요한 시간

if C + B >= 60:
     A += (C + B) // 60
     B = (C + B) % 60
     if A >= 24:
         A-= 24
else:
    B += C

print(A, B)