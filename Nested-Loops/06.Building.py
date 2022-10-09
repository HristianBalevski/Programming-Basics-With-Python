flats_cnt = int(input())
rooms_cnt = int(input())

for flat in range(flats_cnt, 0, - 1):
    for room in range(rooms_cnt):
        if flat == flats_cnt:
            print(f'L{flat}{room}', end=' ')
            if room + 1 == rooms_cnt:
                print()
        elif flat % 2 == 0:
            print(f'O{flat}{room}', end=' ')
            if room + 1 == rooms_cnt:
                print()
        else:
            print(f'A{flat}{room}', end=' ')
            if room + 1 == rooms_cnt:
                print()
