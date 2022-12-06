import schedule
import time
from datetime import datetime

# def job():
#     print('Boo')

# # run job until a 18:30 today
# schedule.every(1).hours.until("20:10").do(job)
# current_time = datetime.now(timezone.utc)

# print(current_time)

# hour = datetime.now().hour   # the current hour
# minute = datetime.now().minute # the current minute
# current_time = hour + minute
# print(hour)
# print(minute)
# print(current_time)

# current_time = datetime.now().second
# print(current_time)

def job():
    start_time = 10
    end_time = 30
    current_time = datetime.now().second
    if current_time < start_time:
        print("I am sleep")
        print(current_time)
    elif current_time >= end_time:
        print('The game is over')
        print(current_time)
    else:
        print('I am awake')
        print(current_time)

schedule.every(5).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

# import schedule
# import time

# def job():
#     print("I'm working...")

# # Run job every 3 second/minute/hour/day/week,
# # Starting 3 second/minute/hour/day/week from now
# schedule.every(3).seconds.do(job)


# while True:
#     schedule.run_pending()
#     time.sleep(1)