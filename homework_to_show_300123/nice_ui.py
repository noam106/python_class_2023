import backend

if __name__ == '__main__':
    while True:
        user_name = input('Hi, please enter your name: ')
        if backend.name_valid(user_name) is False:
            user_name = input('A name should contain only letters, please try again: ')
        if backend.name_netsional(user_name) is False:
            user_input = input(f'{user_name}, that is interesting, i never hared that name before.'
                               f' are you sure its your name? :')
            if user_input.lower() != 'yes':
                continue
        else:
            break

