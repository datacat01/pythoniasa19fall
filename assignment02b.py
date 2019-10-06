"""
Assignment 2-B
==============

Wrap Assignment 1-B in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text()
True
"""

def poem():
    p = 'Вот дом, который построил Джек.\n\n'

    main_dict = {
        ('пшеница', 'пшеницу'): 'Которая в тёмном чулане хранится',
        ('весёлая птица-синица', 'синицу'): 'Которая часто ворует',
        (' кот', 'кота'): 'Который пугает и ловит',
        (' пёс без хвоста', 'старого пса без хвоста'): 'Который за шиворот треплет',
        ('корова безрогая', 'корову безрогую'): 'Лягнувшая',
        ('старушка, седая и строгая', 'коровницей строгою'): 'Которая доит',
        ('ленивый и толстый пастух', 'пастуха'): 'Который бранится с',
        (' два петуха', None): 'Которые будят того'
    }

    introductions = ['А это '+key[0] if key[0][0]!=' ' else 'Вот'+key[0]
                    for key in main_dict.keys()]

    actions = []
    l = list(main_dict.items())

    for i in range(len(l)):
        verb = l[i][1]
        noun = l[i-1][0][1]
        if noun is not None:
            s = f'{verb} {noun},'
        else:
            s = f'{verb}'
        actions.append(s)

    for i in range(len(introductions)):
        actions_i = '\n'.join(actions[:(i+1)][::-1])
        p+=introductions[i]+',\n'+actions_i
        if 'Лягнувшая' in actions_i:
            actions = list(map(lambda repl: repl.replace('Лягнувшая','Лягнувшую'), actions))
        p+='\nВ доме, который построил Джек.\n\n'
    return p[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
