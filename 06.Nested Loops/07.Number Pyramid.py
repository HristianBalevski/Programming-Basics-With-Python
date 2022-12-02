n = int(input())
cnt = 1
is_pyramid_ready = False

for row in range(1, n + 1):
    for col in range(0, row):
        print(f'{cnt}', end=' ')
        cnt += 1

        if cnt > n:
            is_pyramid_ready = True
            break
    if is_pyramid_ready:
        break
    print()
