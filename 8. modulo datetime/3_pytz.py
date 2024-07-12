import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Toronto'))

print(data)
print(data2)