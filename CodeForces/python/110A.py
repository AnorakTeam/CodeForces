number = int(input())

lucky_numbers = 0

while number > 0:
    if number%10 == 4 or number%10 == 7:
        lucky_numbers += 1
    number //= 10

if lucky_numbers == 4 or lucky_numbers == 7:
    print("YES")
else:
    print("NO")
