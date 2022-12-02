month = input()
nights_cnt = int(input())

discount = 0
flat = 0
studio = 0

if month == 'May' or month == 'October':

    studio = nights_cnt * 50
    flat = nights_cnt * 65

    if nights_cnt > 14:

        studio = studio - (studio * 0.30)
        flat = flat - (flat * 0.10)

    elif nights_cnt > 7:
        studio = studio - (studio * 0.05)

if month == 'June' or month == 'September':

    studio = nights_cnt * 75.20
    flat = nights_cnt * 68.70

    if nights_cnt > 14:

        studio = studio - (studio * 0.20)
        flat = flat - (flat * 0.10)

if month == 'July' or month == 'August':
  
    studio = nights_cnt * 76
    flat = nights_cnt * 77

    if nights_cnt > 14:
        flat = flat - (flat * 0.10)

print(f'Apartment: {flat:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
