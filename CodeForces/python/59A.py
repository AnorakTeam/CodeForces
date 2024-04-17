word = input()
uppercases, lowercases = 0, 0

for i in word:
    if ord(i) > 90:
        lowercases += 1
    else:
        uppercases += 1

if lowercases >= uppercases:
    word = word.lower()
else:
    word = word.upper()

print(word)

