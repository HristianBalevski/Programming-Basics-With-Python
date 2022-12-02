name = input()
password = input()

curr_password = ''

while curr_password != password:
    curr_password = input()

    if curr_password == password:
        print(f'Welcome {name}!')