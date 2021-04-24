n = input()

lucky_digit = 0
for digit in n:
    if digit == "4" or digit == "7":
        lucky_digit += 1


if lucky_digit == 4 or lucky_digit == 7:
    print("YES")
else:
    print("NO")