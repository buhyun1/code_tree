Y,M,D = map(int, input().split())

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def is_valid_date(year,month,day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[1] = 29

    if 1<= month<=12 and 1<=day <= days_in_month[month-1]:
        return True
    return False

def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"


def determine_season(year, month, day):
    if is_valid_date(year, month, day):
        return get_season(month)
    else:
        return -1

result = determine_season(Y, M, D)
print(result)