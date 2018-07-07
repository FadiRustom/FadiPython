# Python 2
# Auther: Fadi Rustom

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day<daysInMonth(year, month):
        return year, month, day +1
    else:
        if month<12:
            return year, month +1, 1
        else:
            return year +1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1<year2:
        return True
    if year1==year2:
        if month1<month2:
            return True
        if month1==month2:
            return day1<day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days +=1
    if days <0:
        return "Error is Date2 > Date1", False
    return days

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4   == 0:
        return True
    return False

def daysInMonth(year, month):
    if month ==1 or month ==3 or month==5 or month ==7 or month ==8 or month ==10 or month ==12:
        return 31
    if month ==2:
        if isLeapYear(year):
            return 29
        return 28
    else:
        return 30
    return 30

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print ("Test with data:", args, "failed")
            else:
                print ("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args))            

test()

def myTest():
    ''' Test with True Prog'''
    assert daysBetweenDates (2013,1,1,2013,1,1) == 0
    assert daysBetweenDates (2013,1,1,2013,1,2) == 1
    assert daysBetweenDates (2013,1,1,2014,1,1) == 365
    assert nextDay(2012,2,28) == (2012,2,29)
    assert nextDay(2012,12,31) == (2013,1,1)
    print ('Tests finished')

myTest()
