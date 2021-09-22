res =''
String = int(input())
for i in range(String):
    if i%2==0:
        res +='I hate '
    else:
        res +='I love '
    if i!= String - 1:
        res +='that '
    else:
        res +='it '
print(res)
