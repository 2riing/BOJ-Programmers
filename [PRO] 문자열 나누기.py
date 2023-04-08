# 첫글자 x
# 읽으면서 x와 아닌 다른글자들을 세면서 같아지면 분리
# 반복
# 없으면 종료
def solution(s):
    answer = 0
    xcnt = 1
    cnt = 0
    cur = s[0]
    for i in range(1, len(s)):
        
        if xcnt == 0 and cnt == 0:
            cur = s[i]
            xcnt += 1
        else:
            if s[i] == cur:
                xcnt += 1
            else:
                cnt += 1
        if xcnt == cnt:
            xcnt, cnt = 0, 0
            answer += 1
    if cnt != 0 or xcnt != 0:
        answer += 1
    return answer
