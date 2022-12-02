from math import floor

world_record = float(input())
length = float(input())
time_for_1m = float(input())

slower_time = floor(length / 15) * 12.5
ivan_whole_time = (length * time_for_1m) + slower_time

if ivan_whole_time < world_record:
    print(f'Yes, he succeeded! The new world record is {ivan_whole_time:.2f} seconds.')
else:
    needed_time = ivan_whole_time - world_record
    print(f'No, he failed! He was {needed_time:.2f} seconds slower.')
