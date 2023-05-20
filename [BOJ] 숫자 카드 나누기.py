def gcd(a, b):
    if b % a == 0:
        return a
    return gcd(b % a, a)
        
def solution(arrayA, arrayB):
    answer = 0
    N = len(arrayA)
    
    # 최대 공약수 구해주기
    A, B = arrayA[0], arrayB[0]
    for i in range(N):
        A = gcd(A, arrayA[i])
        B = gcd(B, arrayB[i])
        
    a, b = A, B
    for i in range(N):
        if arrayB[i] % A == 0:
            a = A // gcd(arrayB[i], A)
        if arrayA[i] % B == 0:
            b = B // gcd(arrayA[i], B)

    if a == b: return 0
    elif a > b: return 
