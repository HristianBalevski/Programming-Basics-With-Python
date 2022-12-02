width = int(input())
length = int(input())
height = int(input())

area = width * length * height
boxes = 0
finish = False

data = input()
while data != 'Done':
    info = int(data)
    boxes += info

    if area <= boxes:
        finish = True
        break
    data = input()

if finish:
    if area >= boxes:
        print(f'{area- boxes} Cubic meters left.')
    else:
        print(f'No more free space! You need {boxes - area} Cubic meters more.')
else:
    if area >= boxes:
        print(f'{area- boxes} Cubic meters left.')
    else:
        print(f'No more free space! You need {boxes - area} Cubic meters more.')
