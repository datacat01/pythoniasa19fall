"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    p = 'This is the house that Jack built.\n'

    nouns = [
    'malt', 'rat', 'cat', 'dog', 'cow with the crumpled horn', 'maiden all forlorn',
    'man all tattered and torn', 'priest all shaven and shorn', 'cock that crowed in the morn',
    'farmer sowing his corn'
    ]
    verbs = [
        'ate', 'killed', 'worried', 'tossed', 'milked', 'kissed', 'married', 'waked', 'kept'
    ]

    introductions = [f'\nThis is the {noun}' if noun=='malt'
                else f'\nThis is the {noun},'
                for noun in nouns]
    actions = [f'That {verb} the {noun}' if noun=='malt'
                else f'That {verb} the {noun},'
                for verb,noun in zip(verbs,nouns)]

    for i in range(len(nouns)):
        p += introductions[i]
        if ''.join(actions[:i][::-1]) != '':
            p += '\n'+'\n'.join(actions[:i][::-1])
        p += '\nThat lay in the house that Jack built.\n'
    
    return p[:-1]


if __name__ == '__main__':
    #print(poem())
    import doctest
    doctest.testmod()
