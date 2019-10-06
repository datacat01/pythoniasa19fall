"""
Assignment 1-B (optional)
=========================

This assignment is similar to 1-A except that the poem is in Russian now.

"""

main_dict = {
    ('пшеница', 'пшеницу'): 'Которая в тёмном чулане хранится',
    ('весёлая птица-синица', 'синицу'): 'Которая часто ворует',
    (' кот', 'котa'): 'Который пугает и ловит',
    (' пёс без хвоста', 'старого пса без хвоста'): 'Который за шиворот треплет',
    ('корова безрогая', 'корову безрогую'): 'Лягнувшая',
    ('старушка, седая и строгая', 'коровницей строгою'): 'Которая доит',
    ('ленивый и толстый пастух', 'пастуха'): 'Который бранится с',
    (' два петуха', None): 'Которые будят того'
}

introductions = ['A это '+key[0] if key[0][0]!=' ' else 'Вот'+key[0]
                 for key in main_dict.keys()]

actions = []
l = list(main_dict.items())

for i in range(len(l)):
    verb = l[i][1]
    #print(f'verb: {verb}')
    noun = l[i-1][0][1]
    #print(f'noun: {noun}')

    if noun is not None:
        s = f'{verb} {noun},'
    else:
        s = f'{verb}'
    actions.append(s)

# print(introductions)
# print(actions)

print('Вот дом, который построил Джек.\n')
for i in range(len(introductions)):
    actions_i = '\n'.join(actions[:(i+1)][::-1])
    print(introductions[i]+',\n'+actions_i)
    if 'Лягнувшая' in actions_i:
        actions = list(map(lambda repl: repl.replace('Лягнувшая','Лягнувшую'), actions))
    print('В доме, который построил Джек.\n')
