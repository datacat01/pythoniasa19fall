nouns = [
    "malt", "rat", "cat", "dog", "cow with the crumpled horn", "maiden all forlorn",
    "man all tatter'd and torn", "priest all shaven and shorn", "cock that crow'd in the morn",
    "farmer sowing his corn"
]
verbs = [
    "ate", "kill'd", "worried", "tossed", "milk'd", "kissed", "married", "waked", "kept"
]
data = dict(zip(nouns, verbs))
introductions = [f"\nThis is the {noun}," for noun in nouns]
actions = [f"\nThat {item[1]} the {item[0]}," for item in data.items()]

print("This is the house that Jack built.")
for i in range(len(actions)):
    print(introductions[i]+"".join(actions[:i][::-1]))
    print("That lay in the house that Jack built.")
