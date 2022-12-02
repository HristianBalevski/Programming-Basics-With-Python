number = int(input())

sum_num = 0

while True:
    curr_number = int(input())
    sum_num += curr_number

    if sum_num >= number:
        print(sum_num)
        break