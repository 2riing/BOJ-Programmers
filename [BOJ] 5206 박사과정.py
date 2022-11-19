N = int(input())
for _ in range(N):
  question = input()
  if question == "P=NP":
    print('skipped')
  else:
    a, b = question.split('+')
    print(int(a) + int(b))