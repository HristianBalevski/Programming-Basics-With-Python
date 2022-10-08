favorite_book = input()

is_found = False
books_cnt = 0

current_command = input()
while current_command != 'No More Books':

    if current_command == favorite_book:
        is_found = True
        break

    books_cnt += 1
    current_command = input()

if is_found:
    print(f'You checked {books_cnt} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_cnt} books.')
