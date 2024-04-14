n = int(input())
games = input()

anton, danik = 0, 0

for game in games:
    if game == "A":
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")