import time
t = input().strip()
def convert_time(t):
    # generate the 24 hours format
    return time.strftime("%H:%M:%S", time.strptime(t, "%I:%M:%S%p"))
if __name__=="__main__":
    print(convert_time(t))
