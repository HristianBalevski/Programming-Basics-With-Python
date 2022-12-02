name = input()
grades_cnt = 0
years_cnt = 0
years_failed = 0

while True:
    annual_grade = float(input())
    years_cnt += 1

    if annual_grade < 4:
        years_failed += 1

        if years_failed == 2:
            print(f'{name} has been excluded at {years_cnt} grade')
            break

        years_cnt -= 1

    else:
        grades_cnt += annual_grade

    if years_cnt == 12:
        average_grade = grades_cnt / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break