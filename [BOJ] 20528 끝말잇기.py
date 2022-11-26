def Check():
    start, end = words[0][0], words[0][-1]
    for i in range(1, len(words)):
        if words[i][0] != start or words[i][-1] != end:
            print(0)
            return 
    print(1)
    return 

N = int(input())
words = list(input().split())
Check()


