#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(house_Start,house_Stop,appleT,orangeT,all_apple,all_orange):
    total_apple, total_orange = 0, 0
    for i in all_apple:
        if (i + appleT >= house_Start and i + appleT <= house_Stop):
            total_apple += 1

    for i in all_orange:
        if (i + orangeT >= house_Start and i + orangeT <= house_Stop):
            total_orange += 1

    print(total_apple)
    print(total_orange)


if __name__ == '__main__':
    house_Start, house_Stop = map(int, input().split())
    appleT, orangeT = map(int, input().split())

    apples, oranges = map(int, input().split())

    all_apple = list(map(int, input().split()))
    all_orange = list(map(int, input().split()))
    countApplesAndOranges(house_Start,house_Stop,appleT,orangeT,all_apple,all_orange)
