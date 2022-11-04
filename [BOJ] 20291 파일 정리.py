import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
answer = dict()
answer_list = []
N = int(input())
for _ in range(N):
    files = list(input().split('.'))
    file_type = files[1]
    if file_type in answer.keys():
        answer[file_type] += 1
    else:
        answer[file_type] = 1


for k,v in answer.items():
    answer_list.append([k, v])
answer_list.sort(key=lambda x:x[0])
for answers in answer_list:
    print(*answers)
