from datetime import datetime, timedelta

def parsedate_mdy(text: str):
    return datetime.strptime(text,"%m/%d/%Y")
def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")

text = '12/30/2000'
date_dt =  parsedate_mdy(text)
print(date_dt)
date_str = formatdate_ymd(date_dt)
print(date_str)