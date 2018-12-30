import time
from datetime import datetime

epochSeconds = time.time()
print(epochSeconds)

t = time.ctime(epochSeconds)
print(t)

dt = datetime.today()
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current Time: {}:{}:{}'.format(dt.hour, dt.minute, dt.second))
