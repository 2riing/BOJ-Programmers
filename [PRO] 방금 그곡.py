def solution(m, musicinfos):
    answerList = []
    num = 0
    m = m.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(',')
        startH, startM, endH, endM = start[:2], start[3:], end[:2], end[3:]
        playTime = (int(endH) - int(startH)) * 60 + (int(endM) - int(startM))
        info = info.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

        played = ''
        I = len(info)
        if playTime > I: 
            idx, cnt = 0, 0
            while True:
                if len(played) == playTime: break;
                played += info[idx]
                idx = 0 if idx == I - 1 else idx + 1
        else: played = info[:int(playTime)] 

        if m in played: 
            answerList.append([playTime, num, title])
            num += 1
               
    answerList.sort(key = lambda x: (-x[0], x[1]))
    if answerList: return answerList[0][2]
    else: return "(None)"
