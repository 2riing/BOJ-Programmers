import sys
sys.stdin = open('input.txt')

def DFS(start, mo, ja):
    if len(arr) == L and mo > 0 and ja > 1:
        print(''.join(arr))
        return

    for i in range(start, C):
        if words[i] in mos: # 모음일경우
            arr.append(words[i])
            DFS(i + 1, mo + 1, ja)
            arr.pop()
        else: # 자음일 경우
            arr.append(words[i])
            DFS(i + 1, mo, ja + 1)
            arr.pop()

L, C = map(int, input().split())
words = list(input().split())
words.sort()

mos = ['a', 'e', 'i', 'o', 'u']

mo = 0
ja = 0
arr = []
DFS(0, 0, 0)