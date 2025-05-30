#!/usr/bin/env python3

class Fish():
    def swim(self):
        return print("The fish is swimming")

    def habitat(self):
        return print("The fish lives in water")
    
class Bird():
    def fly(self):
        return print("The bird is flying")

    def habitat(self):
        return print("The bird lives in the sky")
    
class FlyingFish(Fish, Bird):
    def swim(self):
        return print("The flying fish is swimming!")
    
    def fly(self):
        return print("The flying fish is soaring!")

    def habitat(self):
        return print("The flying fish lives both in water and the sky!")
