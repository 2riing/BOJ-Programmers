import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

print(numbers.count(v))