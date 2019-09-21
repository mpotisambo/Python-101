import datetime
from datetime import date
datetime_object = datetime.datetime.now()
print(datetime_object) # prints out the current date and time

date_object = datetime.date.today()
print(date_object) # this is for getting current date-----------------------------


# Datetime.date class-------------------------------------------------------------------------------

d = datetime.date(2019, 4, 13)
print(d)

#Getting date from time stamp-------------------------------------------------------------------------
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

#printing todays year month and day---------------------------------------------------------
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


#time
from datetime import time

a = time()
print("a =", a)# time(hour = 0, minute = 0, second = 0)

b = time(11, 34, 56)
print("b =", b)# time(hour, minute and second)


c = time(hour = 11, minute = 34, second = 56)
print("c =", c)# time(hour, minute and second)


d = time(11, 34, 56, 234566)
print("d =", d)# time(hour, minute, second, microsecond)

#Printing hours, mins, sec, and micro, sec

from datetime import time
a = time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

# date time object------------------------------------------------------------------------------
from datetime import datetime

a = datetime(2018, 11, 28)#datetime(year, month, day)
print(a)

b = datetime(2017, 11, 28, 23, 55, 59, 342380)# datetime(year, month, day, hour, minute, second, microsecond)
print(b)

 #Print year, month, hour, minute and timestamp

from datetime import datetime
a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())