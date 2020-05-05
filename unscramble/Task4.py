import csv
from itertools import chain
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_numbers = list(chain.from_iterable(
    [(sender, reciever) for sender, reciever, _ in texts]))

text_set = set(text_numbers)

call_set = set()
call_recieve = set()

for send, recieve, _, _ in calls:
    call_set.add(send)
    call_recieve.add(recieve)


telemarkerters = call_set - (text_set | call_recieve)

print("These numbers could be telemarketers:")

for tel_number in sorted(telemarkerters):
    print(tel_number)