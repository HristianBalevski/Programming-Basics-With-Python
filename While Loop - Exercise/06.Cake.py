width = int(input())
length = int(input())
cake = width * length
people = 0
finish = False
command = input()

while command != 'STOP':
    guests = int(command)
    people += guests

    if people >= cake:
        finish = True
        break
    command = input()

if finish:
    print(f'No more cake left! You need {people - cake} pieces more.')
else:
    print(f'{cake - people} pieces are left.')