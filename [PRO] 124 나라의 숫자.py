def solution(n):
    answer = ''
    while n:
        # 3으로 나눠떨어지지 않을 경우
        if n % 3 > 0:
            answer += str(n % 3) # 나머지 넣어주고
            n = n // 3 # n값 갱신
        else: # 3으로 나눠떨어짐, 나머지를 4로 해주니까 1빼줌
            answer += "4"
            n = n // 3 - 1
        print(n)
    print(answer)
    return answer[::-1]
[출처] 프로그래머스 124 나라의 숫자 python|작성자 2riing
