def solution(arr):
    answer = [0, 0]
    N = len(arr)
    def quad(x, y, n):
        init = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != init:
                    half = n // 2
                    quad(x, y, half)
                    quad(x + half, y, half)
                    quad(x, y + half, half)
                    quad(x + half, y + half, half)
                    return
        answer[init] += 1
    quad(0, 0, N)
    return answer
