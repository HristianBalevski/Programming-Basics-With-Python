import math
from math import  floor
list_cnt = int(input())
list_per_hour = int(input())
days = int(input())

needed_hour = math.floor(list_cnt / list_per_hour) / days

print(needed_hour)
