import time
import requests
from datetime import datetime
from pytz import timezone
import pytz

pacific = timezone("US/Pacific")

now = datetime.now(tz=pacific)
year = now.year
month = now.month
day = now.day
hour = now.hour
print "now: ", now
print "hour: ", hour
print "day: ", day
print "month: ", month
print "year: ", year
