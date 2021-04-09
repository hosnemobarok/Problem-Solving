import calendar
import datetime


def findDay(date):
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[born].upper())


if __name__=="__main__":
    date = input()
    print(findDay(date))
