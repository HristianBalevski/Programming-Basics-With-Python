import sys

min_number = sys.maxsize

while True:
    command = input()

    if command == 'Stop':
        break

    curr_command = int(command)

    if curr_command < min_number:
        min_number = curr_command

print(min_number)