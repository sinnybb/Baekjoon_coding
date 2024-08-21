length = int(input())
message = str(input())
alphabets = [chr(i) for i in range(97,123)]

summation = 0

for i in range(length):
  if message[i] in alphabets :
    summation += (alphabets.index(message[i]) + 1) * (31 ** i)

print(summation)