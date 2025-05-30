#!/usr/bin/env python3

class SwimMixin():
    def swim(self):
        return print("The creature swims!")


class FlyMixin():
    def fly(self):
        return print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        return print("The dragon roars!")
