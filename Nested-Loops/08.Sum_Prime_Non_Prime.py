command = input()
prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    curr_number = int(command)

    if curr_number < 0:
        print('Number is negative.')
        command = input()
        continue
    if curr_number <= 1:
        non_prime_sum += curr_number
    else:
        is_prime = True
        for div in range(2, curr_number):
            if curr_number % div == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += curr_number
        else:
            non_prime_sum += curr_number
    command = input()
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')