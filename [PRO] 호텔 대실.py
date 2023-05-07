def solution(book_time):
    rooms = []
    book_time.sort()
    
    N = len(book_time)
    for i in range(N):
        start, end = book_time[i]
        startMin = 60 * int(start[:2]) + int(start[3:])
        endMin = 60 * int(end[:2]) + int(end[3:]) + 10 # 청소시간 더해줌
    
        for j in range(len(rooms)):
            s, e = rooms[j]
            if e <= startMin:
                rooms[j][1] = endMin
                break;
        else: rooms.append([startMin, endMin])

    return len(rooms)
