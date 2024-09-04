import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)    # return random number in the range

dice = Dice(6)
print(dice.roll())  # print random number between 1 and 6

dice2 = Dice(14)
print(dice2.roll())  # print random number between 1 and 14
