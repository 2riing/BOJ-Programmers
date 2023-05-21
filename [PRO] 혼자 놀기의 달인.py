def solution(cards):
    answer = []
    N = len(cards)
    visited = [0 for _ in range(N + 1)]
                                
    for v in cards:
        if not visited[v]:
            temp = []
            while v not in temp:
                temp.append(v)
                v = cards[v-1]
                visited[v] = 1
            answer.append(len(temp))

    if len(answer) == 1: return 0 # 1번 상자에 다담김
    else: answer.sort(reverse=True) # 최대 값 정렬 
        
    return answer[0] * answer[1]
