import datetime
mytime = datetime.time(13,20,1,20)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print(mytime.microsecond)
print(type(mytime))
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())
from datetime import datetime
mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)
#DATE
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)
result = date1 - date2
print(date1 - date2)
print(type(result))
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
print(datetime1 - datetime2)
mydiff = datetime1 - datetime2
print(mydiff.seconds)