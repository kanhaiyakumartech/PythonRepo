# I written a code for clender
import calendar

def Check_Day_Name(month, day, year):
    ans = calendar.weekday(year, month, day)
    return calendar.day_name[ans].upper()
