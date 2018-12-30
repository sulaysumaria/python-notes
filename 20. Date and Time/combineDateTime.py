import datetime as dt

d = dt.date(2018, 7, 21)
t = dt.time(12, 45)

dat = dt.datetime.combine(d, t)
print(dat)
