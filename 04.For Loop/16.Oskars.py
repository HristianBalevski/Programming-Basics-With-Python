name_of_actor = input()
points_from_academy = float(input())
jury_cnt = int(input())
jury_name = ''
points_for_actor = points_from_academy
total_points = 0

for name in range(1, jury_cnt + 1):
    curr_name = input()
    grade = float(input())
    points_for_actor += (len(curr_name) * grade) / 2
    
    if points_for_actor > 1250.5:
        print(f'Congratulations, {name_of_actor} got a nominee for leading role with {points_for_actor:.1f}!')
        break
if points_for_actor < 1250.5:
    needed_points = 1250.5 - points_for_actor
    print(f'Sorry, {name_of_actor} you need {needed_points:.1f} more!')
