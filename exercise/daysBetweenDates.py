def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    if(year2 > year1):

        if (month2 > month1):

            if(day2>day1):
                dayOfDay=day2-day1
            elif(day2==day1):
                dayOfDay=0
            else:
                month2=month2-1
                day2=day2+30
                dayOfDay=day2-day1
            minOfMonth = month2 - month1
            dayOfmonth = minOfMonth * 30
        elif(month2== month1):
            if (day2 > day1):
                dayOfDay = day2 - day1
            elif (day2 == day1):
                dayOfDay = 0
            else:
                year2=year2-1
                month2=month2+12
                month2=month2-1
                day2=day2+30
                dayOfDay=day2-day1
            dayOfmonth=0

        else:
            year2=year2-1
            month2=month2+12
            minOfMonth=month2-month1
            dayOfmonth=minOfMonth * 30

        minOfYear = year2 - year1
        dayofyear = minOfYear * 365

    totalofgreater=dayofyear+dayOfmonth+dayOfDay
    return total

print(daysBetweenDates(2000,10,20,2010,12,30))