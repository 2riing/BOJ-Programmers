def solution(storey):
    answer = 0

    while storey > 0:
        cur = storey % 10 # 현재 위치
        if storey < 10: # 제일 큰 자리수일경우
            storey = 0
            if(cur > 5):
                answer += 11 - cur
            else:
                answer += cur
        else: 
            storey = storey // 10 # 한자리 잘라서 저장함
            if(cur > 5):
                answer += 10 - cur
                storey += 1
            # 제일 큰자리수가 아니면서 5인 경우 
            elif cur == 5: # 다음 마지막 숫자가 5 이상인 경우
                if int(str(storey)[-1]) >= 5:
                    answer += 5
                    storey += 1
                else:
                    answer += 5
            else:
                answer += int(cur)
    return answer
