from math import ceil
name_serial = input()
length_ep = float(input())
break_length = float(input())

time_for_lunch = break_length * 1/8
time_for_relax = break_length * 1/4
free_time = break_length - time_for_lunch - time_for_relax

if free_time >= length_ep:
    left_time = ceil(free_time - length_ep)
    print(f'You have enough time to watch {name_serial} and left with {left_time} minutes free time.')
else:
    needed_time = ceil(length_ep - free_time)
    print(f"You don't have enough time to watch {name_serial}, you need {needed_time} more minutes.")
