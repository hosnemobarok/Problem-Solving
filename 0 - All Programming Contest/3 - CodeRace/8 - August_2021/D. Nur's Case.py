main_web = input()

ok_web = main_web.replace("j", "l").replace("!", "l").replace("@", "a").replace("O", "a").replace("o", "a").replace("D", "a").replace("0", "a").replace("e", "a").replace("S", "s").replace("5", "s").replace("2", "s").replace("i", "1").replace("?", "1")
count = 0
ok_web_position = []
for ind in range(int(input())):
    user_web = input()
    temp_user_web = user_web.replace("j", "l").replace("!", "l").replace("@", "a").replace("O", "a").replace("o", "a").replace("D", "a").replace("0", "a").replace("e", "a").replace("S", "s").replace("5", "s").replace("2", "s").replace("i", "1").replace("?", "1")


    if ok_web != main_web and user_web == ok_web:
        ok_web_position.append(ind + 1)
        count += 1

    if temp_user_web == ok_web:
        ok_web_position.append(ind +1)
        count += 1

print(count)
print(*ok_web_position)
