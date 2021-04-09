
def Grading_Students(num):
    if num < 38:
        output = num
    elif num % 5 >= 3:
        output = num + (5-num%5)
    else:
        output = num

    return output


if __name__ == '__main__':
    for _ in range(int(input())):
        num = int(input())
        print(Grading_Students(num))
