#!/usr/bin/env python3

class CountedIterator():
    def __init__(self, iterable_obj):
        self.iterateur = iter(iterable_obj)
        self.count = 0

    def __next__(self):  # iterable_obj = [10, 20, 30]
        value = next(self.iterateur)  # avance ds la liste
        self.count += 1  # on incrémente de 1 à chaque appel
        return value  # on renvoie la valeur lu a chaque appel (ex : 10)

    def __iter__(self):
        # la class elle même est un for
        # on l'utilise pour boucler avec next()
        return self

    def get_count(self):
        return self.count
