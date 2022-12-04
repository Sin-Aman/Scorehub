import schedule
from datetime import datetime, date, time, timezone
# from datetime import datetime, timedelta, time

# def job():
#     print('Boo')

# # run job until a 18:30 today
# schedule.every(1).hours.until("20:10").do(job)
# current_time = datetime.now(timezone.utc)

# print(current_time)

hour = datetime.now().hour   # the current hour
minute = datetime.now().minute # the current minute

print(hour)