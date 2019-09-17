nouns = [
    "malt", "rat", "cat", "dog", "cow with the crumpled horn", "maiden all forlorn",
    "man all tatter'd and torn", "priest all shaven and shorn", "cock that crow'd in the morn",
    "farmer sowing his corn"
]
verbs = [
    "ate", "kill'd", "worried", "toss'd", "milk'd", "kissed", "married", "waked", "kept"
]

introductions = [f"\nThis is the {noun}," for noun in nouns]
actions = [f"That {verb} the {noun}," for verb,noun in zip(verbs,nouns)]

print("This is the house that Jack built.")
for i in range(len(nouns)):
    print(introductions[i]+"\n".join(actions[:i][::-1]))
    print("That lay in the house that Jack built.")
