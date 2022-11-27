import sys
sys.stdin = open('input.txt')

not_self = set()
nums = {i for i in range(10001)}

for i in range(10001):
    total = 0
    total += i
    for j in range(len(str(i))):
        total += int(str(i)[j])
    not_self.add(total)

self_num = sorted(nums - not_self)
for i in range(len(self_num)):
    print(self_num[i])

