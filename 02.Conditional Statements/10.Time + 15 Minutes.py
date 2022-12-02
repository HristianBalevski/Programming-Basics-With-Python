hour = int(input())
minutes = int(input())

extra_minutes = minutes + 15

if extra_minutes > 60:
    hour += 1
    extra_minutes -= 60

elif extra_minutes < 60:
    hour = hour
    extra_minutes = extra_minutes

elif extra_minutes == 60:
    hour += 1
    extra_minutes -= 60

if hour == 24:
    hour -= 24


hour_now = hour // 60
minutes_now = extra_minutes % 60

if extra_minutes < 10:
    print(f'{hour}:{extra_minutes:02d}')
else:
    print(f'{hour}:{extra_minutes}')
