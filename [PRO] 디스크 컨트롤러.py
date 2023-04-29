import heapq
from collections import deque

def Add(q, sec, working):
    while q:
        if q[0][0] > sec: # 현재 시간보다 크다면 skip
            return
        heapq.heappush(working, [q[0][1], q[0][0]]) # 소요 시간 순으로 heapq정렬
        q.popleft()

def solution(jobs):
    N = len(jobs)
    jobs.sort(key=lambda x: x[0]) # 요청 시간 순으로 정렬
    q = deque(jobs)
    sec, time, i = 0, 0, 0 # sec 현재시간 time 누적시간
    working = [] # 작업 대기 

    while i < len(jobs):
        Add(q, sec, working)
        if len(working) > 0:
            current = heapq.heappop(working)
            sec += current[0] # 현재시간
            start = current[1]
            time += (sec - start) # 누적시간 갱신 
            i += 1
        else:
            sec += 1
    return time // N
