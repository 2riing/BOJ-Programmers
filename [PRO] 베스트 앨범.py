def solution(genres, plays):
    answer = []
    album = dict()
    cnt = dict()
    
    N = len(genres)
    for i in range(N):
        if genres[i] in album:
            album[genres[i]].append([plays[i], i])
            cnt[genres[i]] += plays[i]
        else:
            album[genres[i]] = [[plays[i], i]]
            cnt[genres[i]] = plays[i]
            
    cnt_list = []
    for k, v in cnt.items():
        cnt_list.append([v, k])
    cnt_list.sort(key=lambda x: -x[0])
    
    for i in range(len(cnt)):
        album[cnt_list[i][1]].sort(key = lambda x: (-x[0], x[1]))
        N = min(2, len(album[cnt_list[i][1]]))
        for j in range(N):
            answer.append(album[cnt_list[i][1]][j][1])
        
    return answer
