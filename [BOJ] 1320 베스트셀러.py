N = int(input())

books = {}
for _ in range(N):
    temp = input()
    if temp in books:
        books[temp] += 1
    else:
        books[temp] = 1

max_num = 0
max_name = []
for k, v in books.items():
    if v > max_num:
        max_num = v
        max_name= [k]
    elif v == max_num:
        max_name.append(k)

max_name.sort()
print(max_name[0])