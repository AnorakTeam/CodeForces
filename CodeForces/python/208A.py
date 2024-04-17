dubstep = input()
crude_song = ""
for word in list(filter(lambda x: x!="", dubstep.split("WUB"))):
    crude_song += word + " "
print(crude_song)
