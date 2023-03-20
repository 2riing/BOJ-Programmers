def solution(common):
    answer = 0
    N = len(common)
    differ = common[1] - common[0]
    flag = 0 # 공차수열일경우 0
    
    num = 0
    for i in range(2, N):
        if (common[i] - common[i-1] != differ):
            flag = 1
            num = common[i] // common[i-1] # 몫이 공비
            break
    
    if flag:
        answer = common[-1] * num
    else:
        answer = common[-1] + differ
        
    return answer
