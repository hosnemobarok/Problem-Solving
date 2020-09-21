#accept

N = int(input())
sec = N % 60
minutes = N // 60
min = minutes // 60
hor = min // 60
print(hor, minutes, sec)