
def task1(text):
    """
    Take comma separated list of integers and return the list of integers.

    >>> task1('89,9,-789, 0, 1')
    [89, 9, -789, 0, 1]
    """
    l = text.split(',')
    return list(map(int, l))


def task2(text):
    """
    Take space separated list of words and return string of these same words but alphabetically sorted.

    >>> task2('pen pineapple apple pen')
    'apple pen pen pineapple'
    """
    l = sorted(text.split())
    return ' '.join(l)


def task3(text):
    """
    Calculate the number of different letters and digits in the text.

    >>> task3('To study and not think is a waste. To think and not study is dangerous. (Confucius, The Analects, Chapter 1)')
    {'digits': 1, 'letters': 22}

    >>> task3('Найди себе дело по душе и тебе не придётся трудиться ни одного дня в жизни. (Конфуций)')
    {'digits': 0, 'letters': 26}
    """
    unique_val = ''.join(set(text))
    digits = 0
    letters = 0
    for i in unique_val:
        if i.isnumeric() is True:
            digits += 1
        elif i.isalpha() is True:
            letters +=1
    return {'digits': digits, 'letters': letters}


def task4(digit, n=4):
    """
    For any digit X from 0 to 9, calculate expression 'X + XX + XXX + XXXX'.

    >>> [task4(d) for d in '0123456789']
    [0, 1234, 2468, 3702, 4936, 6170, 7404, 8638, 9872, 11106]
    """
    if 0<=int(digit)<=9:
        return sum([int(digit*i) for i in range(1, n+1)])


def task5(text, letter1, letter2):
    """
    You are given three inputs: a string, one letter, and a second letter.
    Write a function that returns True if every instance of the first letter
        occurs before every instance of the second letter.

    >>> task5('a rabbit jumps joyfully', 'a', 'j')
    True
    >>> task5('knaves knew about waterfalls', 'k', 'w')
    True
    >>> task5('happy birthday', 'a', 'y')
    False
    >>> task5('happy birthday', 'a', 'z')
    False
    >>> task5('happy birthday', 'z', 'a')
    False
    """
    return -1 < text.rfind(letter1) < text.find(letter2)


def task6(text, censored):
    """
    Given the censored text and the list of censored letters, output the uncensored text.

    >>> task6('Wh*r* d*d my v*w*ls g*?', 'eeioeo')
    'Where did my vowels go?'
    >>> task6('abcd', '')
    'abcd'
    >>> task6('*PP*RC*S*', 'UEAE')
    'UPPERCASE'
    """
    return ''.join(
            ''.join(t) for t in zip(text.split('*'), [*censored, ''])
    )


def task7(text, words):
    """
    Write a function that returns True if a given text can generate an array of words.
        All strings are case insensitive.

    >>> task7('Justin Bieber', ['injures', 'ebb', 'it'])
    True
    >>> task7('Natalie Portman', ['ornamental', 'pita'])
    True
    >>> task7('Chris Pratt', ['chirps', 'rat'])
    True
    >>> task7('Jeff Goldblum', ['jog', 'meld', 'bluffs'])
    False
    """
    return all([set(w.lower()) == set(text.lower()).intersection(w.lower()) for w in words])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
