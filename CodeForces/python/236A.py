nickname = input()

characters = []

for i in range(len(nickname)):
    if nickname[i] not in characters:
        characters.append(nickname[i])

if len(characters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

