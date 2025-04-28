# datetime modules

import datetime

print(datetime.date.today())

date = datetime.date(2025, 4, 23)
print(f"date : {date}")

time = datetime.time(10, 4, 23)
print(f"time : {time}")
now = datetime.datetime.now()
print(now)
modifed_date_time = now.strftime("%H:%M:%S %d-%m-%Y")
print(modifed_date_time)

target_date_time = datetime.datetime(2030, 1, 1, 1, 1, 1)

if target_date_time < now:
    print("Target date has passed")
else:
    print("Target date has not passed")