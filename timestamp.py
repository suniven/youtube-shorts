import re
import sys
import os
import time
import datetime


def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M'
    # format = '%Y-%m-%d %H:%M:%S'
    # value 为时间戳值,如:1460073600.0
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


def datetime_timestamp(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M'))
    return int(round(s))


def get_now_timestamp():
    return datetime_timestamp(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

# d = datetime_timestamp('2022-05-01 08:00')
# print(d)
# s = timestamp_datetime(1460073600)
# print(s)
# print(get_now_timestamp())
