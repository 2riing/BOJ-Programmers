# 아파트의 개수 n, stations의 위치, 전파 도달거리 w
# s는 기지국 번호 num,  i는 index
def solution(n, stations, w):
    answer = 0
    i, s = 0, 1
    while s <= n:
        if i < len(stations) and s >= stations[i] -w and s <= stations[i] + w :
            s = stations[i] + w + 1
            i += 1
        else:
            s += 2 * w + 1
            answer += 1
    return answer
[출처] 기지국 설치 python|작성자 2riing
