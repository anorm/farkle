#!/usr/bin/env python

import random

class Dice:
    value = 0

    def roll(self):
        self.value = random.randint(1, 6)

    def __repr__(self):
        return "({0})".format(self.value)

class Turn:
    def __init__(self):
        self.dice = [Dice() for x in xrange(6)]
        for d in self.dice:
            d.roll()

class Game:
    def __init__(self):
        pass

    @staticmethod
    def valueOf(diceList):
        sortedDice = sorted(diceList, key=lambda x: x.value)
        return sortedDice


class AIPlayer:
    def __init__(self):
        pass


turn = Turn()

print(Game.valueOf(turn.dice))

