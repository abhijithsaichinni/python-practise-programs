def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    leapno = is_year_leap(year)
    if (month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        res=31
    elif (month == 4 or 6 or 9 or 11):
        res=30
    elif (month ==2):
        if (leapno == True):
            res=29
        else:
            res=28
    return res
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    print(result)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
