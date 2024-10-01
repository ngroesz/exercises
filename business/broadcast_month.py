#!/usr/bin/env python

import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

def broadcast_month(date):
  dow = datetime.isoweekday(date)
  if dow > date.day:
    return (date - relativedelta(months=1)).replace(day=1)
  else:
    return date.replace(day=1)


if __name__ == '__main__':
  date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
  print(broadcast_month(date))
