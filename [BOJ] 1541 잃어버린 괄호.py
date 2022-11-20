import sys
sys.stdin = open('input.txt')

words = list(input())
signals = ['0']
numbers = []
num = ''
for i, word in enumerate(words):
    if word.isdigit():
        num += word
    else:
        numbers.append(int(num))
        num = ''
        signals.append(word)
if num:
    numbers.append(int(num))

print(signals, numbers)

numbers.sort(reverse=True)

for i in range(1, len(numbers)):
    pass