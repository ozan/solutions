import calendar

print(sum(calendar.weekday(y, m+1, 1) == 6 for y in range(1901, 2001) for m in range(12)))
