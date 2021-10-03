import os, sys
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

print(os.getcwd())

today = datetime.today()

print(today)

date = today - relativedelta(days= 20)

str_date = date.strftime("%Y-%m-%d")

print(str_date)

obj_date = datetime.strptime(str_date, "%Y-%m-%d")

print(obj_date)