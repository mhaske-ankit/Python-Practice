# module2.py

from module1 import add  # Import the correct function
from module1 import multi


print(add(10, 20))  # Use the renamed function 'add'

print(multi(5, 5))

import datetime
import calendar


today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

