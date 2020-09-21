#not Accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1096

i=1
j = 7
a = 0
while(i<=9):
    print("I=%d J=%d"%(i, j))
    j-=1
    if(j==4):
        a += 1
        j=7
        i=a*3
