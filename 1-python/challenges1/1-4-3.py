from dateutil import parsedate_mdy,formatdate_ymd
from datetime import datetime, timedelta

text = "12/30/2000"
date_dt = parsedate_mdy(text)
assert date_dt == datetime(2000, 12, 30)

date_str = formatdate_ymd(date_dt)
assert date_str == "2000-12-30"

print("All tests passed!")