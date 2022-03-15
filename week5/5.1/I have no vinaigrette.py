import time
import random
from datetime import datetime
"""
I have no vinaigrette!.
By: Eliad Karni.

The Project generates a date between two received dates.
If the generated day is not a SHOPPING_DAY, it prints NO_VINAIGRETTE_DATE_OUTPUT message.

used websites help:
shopping day check -> https://www.delftstack.com/howto/python/python-datetime-day-of-week/
                      https://www.geeksforgeeks.org/python-datetime-strptime-function/
generate date -> https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
"""

TIME_FORMAT = '%Y-%m-%d'
SHOPPING_DAY = 0  # monday: 0, sunday: 6
NO_VINAIGRETTE_DATE_OUTPUT = "I have no vinaigrette!"


def generate_date(earliest: str, latest: str) -> str:
    """
    The function receiving start date and end date, returns a generated date
    between those dates .
    :param earliest: The start date in TIME_SYNTAX syntax.
    :param latest: The end date in TIME_SYNTAX syntax.
    return generated date between the received dates.
    """
    earliest_time = time.mktime(time.strptime(earliest, TIME_FORMAT))
    latest_time = time.mktime(time.strptime(latest, TIME_FORMAT))
    rand_time = earliest_time + (random.random() * (latest_time - earliest_time))
    return time.strftime(TIME_FORMAT, time.localtime(rand_time))


def is_shopping_day(date) -> bool:
    """
    The function returns if the received date is a SHOPPING_DAY
    :param date The checked date in TIME_SYNTAX syntax.
    """
    return datetime.strptime(date, TIME_FORMAT).weekday() == SHOPPING_DAY


if __name__ == '__main__':
    rand_date = generate_date(input("please enter start date:"), input("please enter end date: "))
    print(f"date generated is: {rand_date}")
    if not is_shopping_day(rand_date):
        print(NO_VINAIGRETTE_DATE_OUTPUT)
