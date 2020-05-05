from collections import defaultdict
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
final_dict = defaultdict(int)

for sender, reciever, timetamp, lapse in calls:
    date = datetime.strptime(timetamp, "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        final_dict[sender] += int(lapse)
        final_dict[reciever] += int(lapse)


max_time_spent = max(final_dict.items(), key=lambda x: x[1])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*max_time_spent))