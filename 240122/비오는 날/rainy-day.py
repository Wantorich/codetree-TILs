from datetime import datetime

class Weather :
    def __init__(self, date, day, weather) :
        self.date = date
        self.day = day
        self.weather = weather

    def print_(self) :
        print(self.date, self.day, self.weather, sep=' ')

n = int(input())
weathers = []
date_diffs = []
date_now = datetime.now()
index = -1
for i in range(n) :
    date, day, weather = input().split()
    if weather == 'Rain' :
        y, m, d = map(int, date.split('-'))
        date_cmp = datetime(y,m,d)
        date_diffs.append(date_cmp - date_now)
        weathers.append(Weather(date,day,weather))

index = date_diffs.index(min(date_diffs))
weathers[index].print_()