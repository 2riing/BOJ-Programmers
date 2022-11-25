N = int(input()) 

num = 666

while True:
    num += 1
    if '666' in str(num):
        N -= 1
    if N == 1: 
        print(num)
        break


    