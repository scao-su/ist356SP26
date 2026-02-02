from datetime import datetime, timedelta
today = datetime.now()
print(today)
print(today.day)

birthday = "1/23/2022"
test = datetime.strptime(birthday,"%m/%d/%Y")
print(test)
test = test + timedelta(days = 1)
print(test)