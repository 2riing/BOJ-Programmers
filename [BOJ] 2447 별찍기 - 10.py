import sys
sys.stdin = open('input.txt')

def Draw(n):
    if n == 1:
        return '*'

    Stars = Draw(n//3)
    arr = []

    for star in Stars:
        arr.append(star * 3)
    for star in Stars:
        arr.append(star + ' ' * (n//3) + star)
    for star in Stars:
        arr.append(star*3)

    return arr


N = int(input())
print('\n'.join(Draw(N)))