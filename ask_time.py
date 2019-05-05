from datetime import datetime
from pytz import timezone


def ask_time_action():
    now = datetime.now(timezone('Europe/Paris'))
    response = "Il est {} heure {}".format(now.hour, now.minute)
    return response
