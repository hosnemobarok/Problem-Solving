# problem link: https://www.codechef.com/YTPP001/problems/EOMUL


# In the first example, 24/3=8. As 8 is even so we print 0.
# In the second example, 15/3=5. As 5 is odd so we print 1.
# In the third example, 16 is not divisible by 3, so we print −1

n = int(input())
if n % 3 == 0:
    if n % 2 == 0:
        print(0)

    else:
        print(1)
else:
    print(-1)