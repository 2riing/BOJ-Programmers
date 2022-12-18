import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(T):
    people = []
    N = int(input())
    people = [[int(x) for x in map(int, input().split())] for _ in range(N)]
    people.sort()
    min_rank = people[0][1]
    cnt = 1
    for i in range(1, len(people)):
        rank = people[i][1]
        if min_rank >= rank:
            min_rank = rank
            cnt += 1
    print(cnt)

