#Dimikoj accept

t = int(input())
for i in range(1, t+1):
    trun, crun, rball  = map(int, input().split())

    rrun = (trun - crun) + 1
    pball = 300 - rball
    crr = crun/(pball/6)
    rr = rrun /(rball/6)
    if crun > trun:
        rr = 0.00
    print('%.2f' % crr, ' %.2f' % rr,sep='')



#2nd niom
T = int(input())
for i in range(T):
    N  = list(map(int,input().split()))
    r1 = N[0]
    r2 = N[1]
    b  = N[2]
    current_rr = (r2/(300-b)) * 6
    asking_rr  = ((r1-r2+1)/b) * 6
    if asking_rr < 0:
        asking_rr = 0.00
    print("%.2f %.2f"%(current_rr,asking_rr))
