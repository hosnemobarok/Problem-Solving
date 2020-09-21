#Accept
a,b = map(int, input().split())
if(a>b or a==b):
    print("O JOGO DUROU %d HORA(S)"%(24-a+b))
elif(b>a):
    print("O JOGO DUROU %d HORA(S)"%(b-a))