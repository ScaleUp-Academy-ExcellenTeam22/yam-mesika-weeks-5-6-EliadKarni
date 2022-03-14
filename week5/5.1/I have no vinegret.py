import time
import random
from datetime import datetime
"""
I have no vinegret!.
By: Eliad Karni.

The Project generates a date between two received dates.
If the generated day is not a SHOPPING_DAY, it prints NO_VINEGRETE_DATE_OUTPUT message.

used websites help:
shopping day check -> https://www.delftstack.com/howto/python/python-datetime-day-of-week/
                      https://www.geeksforgeeks.org/python-datetime-strptime-function/
generate date -> https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
"""
#=============================== consts section ===============================
TIME_SYNTAX = '%Y-%m-%d'
SHOPPING_DAY = 0 #monday: 0, sunday: 6
NO_VINEGRET_DATE_OUTPUT = "I have no vinegret!"
#============================== function section ==============================
#------------------------------------------------------------------------------
def generate_date(start:str, end:str):
    """
    The function receiving start date and end date, returns a generated date
    between those dates .
    :param start: THe start date in TIME_SYNTAX syntax.
    :param end: The end date in TIME_SYNTAX syntax.
    return generated date between the received dates.
    """
    stime = time.mktime(time.strptime(start, TIME_SYNTAX))
    etime = time.mktime(time.strptime(end, TIME_SYNTAX))
    #stime + (generated presents of range between the two received dates)
    rand_time = stime + (random.random() * (etime - stime))
    
    return time.strftime(TIME_SYNTAX, time.localtime(rand_time))

#------------------------------------------------------------------------------
def is_shopping_day(date):
    """
    The function returns if the received date is a SHOPPING_DAY
    :param date The checked date in TIME_SYNTAX syntax.
    """
    return (datetime.strptime(date,TIME_SYNTAX).weekday() == SHOPPING_DAY)

#================================= main section ===============================
rand_date = generate_date(input("please enter start date:"), input("please enter end date: "))
print(f"date generated is: {rand_date}")
if(not is_shopping_day(rand_date)):
    print(NO_VINEGRET_DATE_OUTPUT)
