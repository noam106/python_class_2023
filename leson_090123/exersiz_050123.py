def calc_box_surface_and_volume(a: float, b: float, c: float) -> dict[str, float]:
    resulte_dict = {}
    s = 2*(a*b + b*c + a*c)
    v = a*b*c
    resulte_dict['surface'] = s
    resulte_dict['volume'] = v
    return resulte_dict


def is_common(s1: str, s2: str) -> bool:
    for leter in s1:
        if leter in s2:
            return True
    return False


def revers_string(word: str) -> str:
    return word[::-1]


def is_palindrome(s1: str) -> bool:
    if s1 == s1[::-1]:
        return True
    else:
        return False


def is_palindrome_user():
    user_word = input('Pleas enter your word: ')
    if is_palindrome(user_word) is True:
        return 'your word is palindrome'
    else:
        return 'Your word is not a palindrome'


# def primes_up_to_n(n: int) -> int:
#     count = 0
#     for i in range(n+1):
#         if i%2=0:

