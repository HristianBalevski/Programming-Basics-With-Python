import sys

max_number = -sys.maxsize

while True:
    command = input()

    if command == 'Stop':
        break

    curr_command = int(command)

    if curr_command > max_number:
        max_number = curr_command

print(max_number)