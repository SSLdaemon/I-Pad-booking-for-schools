import os
import django
from datetime import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking.settings')
django.setup()

from booking.models import Period

# Create periods
periods = [
    (time(7, 30), time(8, 10)),
    (time(8, 10), time(8, 50)),
    (time(8, 50), time(9, 30)),
    (time(9, 30), time(10, 10)),
    (time(10, 10), time(10, 50)),
    (time(10, 50), time(11, 30)),
    (time(11, 30), time(12, 10)),
    (time(12, 10), time(12, 50)),
    (time(12, 50), time(13, 30)),
    (time(13, 30), time(14, 10)),
    (time(14, 10), time(14, 50)),
    (time(14, 50), time(15, 30)),
]

for start_time, end_time in periods:
    Period.objects.create(start_time=start_time, end_time=end_time)

print("Periods created successfully.")