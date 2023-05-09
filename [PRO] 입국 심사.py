def solution(n, times):
    answer = 0
    
    # 정렬, 최소 최대 값
    times.sort()
    minTime, maxTime = times[0], times[-1] * n 
    
    while True:
        if minTime > maxTime:
            break;
        
        # 현재 선택된 소요시간 
        curTime = (minTime + maxTime) // 2 
        people = 0
        
        # 소요시간동안 심사 가능한 사람 수 
        for time in times:
            people += curTime // time
            if people >= n:
                break;
                
        # 예상한 사람 보다 더 많으면
        if people >= n: 
            answer = curTime
            maxTime = curTime - 1
        elif people < n:
            minTime = curTime + 1
            
    return answer
