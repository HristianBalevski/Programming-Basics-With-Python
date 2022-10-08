bad_grades = int(input())
bad_grades_counter = 0
score_counter = 0
number_of_problems = 0
last_problem = ''

while True:
    name_of_task = input()
    if name_of_task == 'Enough':
        print(f'Average score: {score_counter / number_of_problems:.2f}')
        print(f'Number of problems: {number_of_problems}')
        print(f'Last problem: {last_problem}')
        break
    evaluation = int(input())

    if evaluation <= 4:
        bad_grades_counter += 1
    if bad_grades_counter == bad_grades:
        print(f'You need a break, {bad_grades_counter} poor grades.')
        break
    number_of_problems += 1
    last_problem = name_of_task
    score_counter += evaluation