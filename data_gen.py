import csv
import datetime
import string
import random
import os
import schedule
import time
now = datetime.datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")
print("date and time =", dt_string)

def create_csv():
    with open('data'+dt_string+'.csv', 'w',newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        N = 7
        print("Before writing csv")
        for _ in range(10):
            value = random.randint(0, 1000)
            res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value, res_str, random_date])
        print("CSV file created")

while True:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    create_csv()
    time.sleep(300)