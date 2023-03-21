def binary(num, N):
    bin_num = bin(num)[2:]
    if len(bin_num) < N:
        bin_num = (N - len(bin_num)) * '0' + bin_num
    return bin_num
            
def solution(n, arr1, arr2):
    answer = []
    N = len(arr1)
    for i in range(N):
        arr1_bin = binary(arr1[i], N)
        arr2_bin = binary(arr2[i], N)
        cals = bin(int(arr1_bin, 2) | int(arr2_bin, 2))[2:]
        if len(cals) < N:
            cals = (N - len(cals)) * '0' + cals
        temp = ''
        for j in range(N):
            if cals[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer
