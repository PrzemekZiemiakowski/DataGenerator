import random
from random import randrange
from datetime import timedelta
from datetime import datetime
def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def startAndEndGen():
    d1 = datetime.strptime('1/1/2021 09:15:32', '%d/%m/%Y %H:%M:%S')
    d2 = datetime.strptime('1/1/2022 16:15:32', '%d/%m/%Y %H:%M:%S')
    start=random_date(d1,d2)
    randInt=random.randint(7,40)
    end=start+timedelta(days=randInt)
    return start,end

