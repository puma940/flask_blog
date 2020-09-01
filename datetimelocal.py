from datetime import datetime
import pytz # $ pip install pytz

print(datetime.now(pytz.timezone("Europe/Warsaw")))
