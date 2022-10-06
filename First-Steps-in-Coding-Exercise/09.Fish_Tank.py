length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

total_water = (length * width * height) * 0.001
busy_percent = total_water * percent
needed_water = total_water - busy_percent

print(needed_water)
