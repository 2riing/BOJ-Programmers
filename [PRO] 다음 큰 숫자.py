def solution(n):
    answer = 0
    i = 1
    N = bin(n).count('1')

    while True:
        new_number = n + i
        i += 1
        if bin(new_number).count('1') == N:
            return new_number
