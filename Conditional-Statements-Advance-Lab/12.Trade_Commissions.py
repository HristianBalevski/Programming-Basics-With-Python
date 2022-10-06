city = input()
sales = float(input())

commissions = 0

if city == 'Sofia' or city == 'Varna' or city == 'Plovdiv':

    if city == 'Sofia':

        if 0 <= sales <= 500:
            commissions = sales * 0.05
            print(f'{commissions:.2f}')

        elif 500 < sales <= 1000:
            commissions = sales * 0.07
            print(f'{commissions:.2f}')

        elif 1000 < sales <= 10000:
            commissions = sales * 0.08
            print(f'{commissions:.2f}')

        elif sales > 10000:
            commissions = sales * 0.12
            print(f'{commissions:.2f}')
        else:
            print('error')

    if city == 'Varna':

        if 0 <= sales <= 500:
            commissions = sales * 0.045
            print(f'{commissions:.2f}')

        elif 500 < sales <= 1000:
            commissions = sales * 0.075
            print(f'{commissions:.2f}')

        elif 1000 < sales <= 10000:
            commissions = sales * 0.10
            print(f'{commissions:.2f}')

        elif sales > 10000:
            commissions = sales * 0.13
            print(f'{commissions:.2f}')
        else:
            print('error')

    if city == 'Plovdiv':

        if 0 <= sales <= 500:
            commissions = sales * 0.055
            print(f'{commissions:.2f}')

        elif 500 < sales <= 1000:
            commissions = sales * 0.08
            print(f'{commissions:.2f}')

        elif 1000 < sales <= 10000:
            commissions = sales * 0.12
            print(f'{commissions:.2f}')

        elif sales > 10000:
            commissions = sales * 0.145
            print(f'{commissions:.2f}')
        else:
            print('error')

else:
    print('error')
