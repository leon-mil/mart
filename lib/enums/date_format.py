#! /usr/local/bin/python3

from enum import auto
from strenum import StrEnum

class DateFormat(StrEnum):
    YEAR = 'year',
    MONTH = 'month',
    WEEK = 'week',
    DAY = 'day',
    HOUR = 'hour',
    MIN = 'min',
    SEC = 'sec',
    MICROSECOND = 'mic',
    MILLISECOND = 'mil'