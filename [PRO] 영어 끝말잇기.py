def solution(n, words):
    answer = []

    arr = []
    bucket = [0 for _ in range(n)]
    bucket[0] += 1
    arr.append(words[0])
    
    for i in range(1, len(words)):
        bucket[i % n] += 1
        
        if words[i-1][-1] != words[i][0] or (words[i] in arr):
            return [i % n + 1, bucket[i % n]]
        arr.append(words[i])

    return [0,0]