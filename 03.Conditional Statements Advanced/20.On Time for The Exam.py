exam_hour = int(input())
exam_min = int(input())
hour_arrival = int(input())
min_arrival = int(input())

exam_total_hours = exam_hour * 60 + exam_min
arrival_total_hours = hour_arrival * 60 + min_arrival

time_diff = abs(exam_total_hours - arrival_total_hours)

if arrival_total_hours > exam_total_hours:
    print('Late')

    if time_diff >= 60:
        hours_late = time_diff // 60
        min_late = time_diff % 60

        print(f'{hours_late}:{min_late:02d} hours after the start')
    else:
        print(f'{time_diff} minutes after the start')

elif arrival_total_hours <= exam_total_hours and time_diff <= 30:
    print('On Time')

    if time_diff > 0:

        print(f'{time_diff} minutes before the start')
else:
    print('Early')

    if time_diff >= 60:
        hours_early = time_diff // 60
        min_early = time_diff % 60

        print(f'{hours_early}:{min_early:02d} hours before the start')
    else:
        print(f'{time_diff} minutes before the start')
