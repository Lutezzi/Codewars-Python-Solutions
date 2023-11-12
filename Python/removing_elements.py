def remove_every_other(list):
    return [i for e,i in enumerate(list) if e % 2 == 0]