N, K = map(int, input().split()) # 학생수, 구간 수
S = list(map(int, input().split())) # 학생들 성적
for i in range(K):
    A, B = map(int, input().split())
    stuNum = B - A + 1
    total = 0
    for j in range(A-1, B):
        total += S[j]
    print(round(total / stuNum, 2))
