import datetime

m1, d1, m2, d2 = map(int, input().split())
A = str(input().strip())
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
target_day_index = days_of_week.index(A)

start_date = datetime.date(2024,m1,d1)
end_date = datetime.date(2024, m2, d2)

cnt = 0
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() == target_day_index:
        cnt += 1
    current_date += datetime.timedelta(days = 1)

print(cnt)