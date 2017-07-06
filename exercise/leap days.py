# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def isLeapYear(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


def daysInMonth(year, month):
    if month == 2:  # February
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        listOfMonths = [None, 31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return listOfMonths[month]


def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return (year, month, day + 1)
    elif month == 12:
        return (year + 1, 1, 1)
    else:
        return (year, month + 1, 1)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    return (year1, month1, day1) < (year2, month2, day2)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
        year1, month1, day1 = nextDay(year1, month1, day1)
    return days


# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")


test()
