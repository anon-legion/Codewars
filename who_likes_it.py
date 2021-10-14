def likes(names):
    who = []
    for i, name in enumerate(names):
        if len(who) == 2 and len(names) - i > 1:
            who.append(f'{len(names) - i} others')
            break
        else:
            who.append(name)
    match len(who):
        case 0:
            return 'no one likes this'
        case 1:
            return f'{who[0]} likes this'
        case _:
            return f'{", ".join(who[:-1])} and {who[-1]} like this'


# test = ['Alex', 'Jacob', 'Mark', 'Max']
# print(likes(test))