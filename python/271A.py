year = int(input())

units = tens = hundreds = thousands = 0

while True:
    year += 1
    units = year%10
    tens = (year//10)%10
    hundreds = (year//100)%10
    thousands = year//1000

    # torre administrativa go brrrrrrrrrrrrrrrrr
    if units != tens and units != hundreds and units != thousands and tens != hundreds and tens != thousands and hundreds != thousands:
        break

print(year)