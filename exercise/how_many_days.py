days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    i=1
    while True:
        if(i<len(days_in_month)):
            print(days_in_month[month_number-1])
        break
        i=i+1

def how_many_days2(month_number):
   return days_in_month[month_number-1]

how_many_days(10)

