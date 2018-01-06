#!/usr/bin/env python3

from datetime import date, datetime, timedelta
from icalendar import Calendar, Event
from logging import warn
from uuid import uuid4

import sys


"""
Unknown: how to print an ics file
Data: input is one line separated for each date.
plan1: read stdin, one line at a time, print ics when EOF
downfall: won't detect if schedule is not exactly 1 year
plan2: read all stdin into memory, count # of lines, output if input is correct
downfall: won't start moving until everything inputted
but who cares, compilers work the same way.
plan3: read first line to infer calendar name
Unknown 2: how to generate all-day events
plan4: switch from datetime to date
Unknown 3: how to generate current timestamp for DTSTAMP
plan5: use datetime.datetime.utcnow()
"""

ts = datetime.utcnow()

cal = Calendar()
cal.add('prodid', '-//Bible Schedule//bible_schedule.py v2.0//EN')

dates = [date(2018,1,1)+timedelta(days=n) for n in range(365)]
summaries = sys.stdin.readlines()
if len(summaries) != 365:
    warn('%d days in a year' % len(summaries))

# Guess which testament we're reading.
calname = ('Old Testament' if summaries[0][0] == 'G' else
    'New Testament' if summaries[0][0] == 'M' else
    None)
if calname: cal.add('x-wr-calname', calname)

for d, s in zip(dates, summaries):
    event = Event()
    event.add('summary', s.strip())
    event.add('dtstart', d)
    event.add('dtstamp', ts)
    event.add('rrule', {'freq': 'yearly'})
    event.add('transp', 'TRANSPARENT')
    event.add('uid', uuid4())
    cal.add_component(event)
print(cal.to_ical().decode('utf-8'), end='')
