"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

year = datetime.today().year
month = datetime.today().month
options = sys.argv

if len(options) < 2:
    calendar.prmonth(year, month, w=3, l=1)
elif len(options) < 3:
    if int(options[1]) > 12 or int(options[1]) < 1:
        print('Please enter a valid month from 1 - 12')
    else:
        month = int(options[1])
        calendar.prmonth(year, month, w=3, l=1)
elif len(options) < 4:
    if int(options[1]) > 12 or int(options[1]) < 1:
        print('Please enter a valid month from 1 - 12')
    else:
        year = int(options[2])
        month = int(options[1])
        calendar.prmonth(year, month, w=3, l=1)
else:
    print('Please pass the year and date you\'d like to see. Ex. 14_cal.py 5 2019')
