import backend
import string

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
    joke = backend.chack_noris_fact()
    user_mode = input(f'{user_name}, would you mined tell me how do you feel today? ')
    user_emotion = backend.text2emotikon(user_mode)
    # print(user_emotion)
    # print(type(user_emotion))
    strong_emotion = ""
    grade = 0
    for emotion,i in user_emotion.items():
        if i >= grade:
            strong_emotion = emotion
            grade = i
    if grade == 0:
        print(f'It seems that you have no feeling in your text, but let me tell you a Chuck Norris fact.\n'
              f'it go something like that:\n'
              f'{joke}')
    else:
        print(f'it seems you feel {strong_emotion} today, i have just the right Chuck Norris fact for you.\n'
              f'Here it come:\n'
              f'{joke}')

