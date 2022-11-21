import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
d=dict()
n=int(input())
for line in range(n):
    name,exe=input().strip().split('.')
    d[exe] = d.get(exe,0) + 1
    print(d)
# print(' '.join(a+' '+str(d[a]) for a in sorted(d.keys())))