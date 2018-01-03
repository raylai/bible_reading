#!/usr/bin/env python3

from datetime import datetime, timedelta
from icalendar import Calendar, Event
from logging import warn

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
"""

summaries = sys.stdin.readlines()
if len(summaries) != 365:
    warn('%d days in a year' % len(summaries))

# Guess which testament we're reading.
if summaries[0][0] == 'G':
    calname = 'Old Testament'
elif summaries[0][0] == 'M':
    calname = 'New Testament'
else:
    calname = None

cal = Calendar()
cal.add('prodid', '-//Bible Schedule//bible_schedule.py v2.0//EN')
if calname: cal.add('x-wr-calname', calname)

date = datetime(2018,1,1)
for summary in summaries:
    event = Event()
    event.add('summary', summary.strip())
    event.add('dtstart', date)
    event.add('dtstamp', date)
    event.add('rrule', {'freq': 'yearly'})
    cal.add_component(event)
    date += timedelta(days=1)
print(cal.to_ical().decode('utf-8'), end='')
