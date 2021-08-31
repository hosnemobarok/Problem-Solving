xy = input()
i = xy.index(".")

x = int(xy[:i])
y = int(xy[i+1:])


if 0 <= y <= 2:
    print(x,"-", sep="")
elif 3 <= y <= 6:
    print(x)
else:
    print(x,"+", sep="")