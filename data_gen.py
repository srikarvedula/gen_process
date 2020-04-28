import csv
import datetime
import string
import random
import os
import schedule
import time

def randomword(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


now = datetime.datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")
def create_csv():
    filename='data'+dt_string+'.csv'
    with open(filename, 'w',newline="") as csvfile:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        N = 7
        print("Before writing csv")
        for _ in range(10):
            if _ == random.randint(0, 20) and _ == 2:
                res_str = randomword(30)
            else:
                res_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

            value = random.randint(0, 1000)
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([value, res_str, random_date])
        print("CSV file created")

while True:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    create_csv()
    time.sleep(15)