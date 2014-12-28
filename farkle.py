#!/usr/bin/env python

import random
import collections

class Dice:
    value = 0

    def roll(self):
        self.value = random.randint(1, 6)

    def __repr__(self):
        return "({0})".format(self.value)

class Turn:
    def __init__(self):
        self.dice = [Dice() for x in xrange(6)]
        self.result = None
        self.score = 0

    def take(self):
        if len(self.dice) == 0:
            self.result = False
            return False
        for d in self.dice:
            d.roll()
        self.dice = sorted(self.dice, key=lambda x: x.value)
        if Game.valueOf(self.dice) == 0:
            self.result = False
            return False
        self.result = True
        return True

class Game:
    def __init__(self):
        self.players = []
        
    def addPlayer(self, player):
        self.players.append(player)
    
    def run(self):
        for player in self.players:
            player.score = 0
            
        while max(player.score for player in self.players) < 10000:
            for player in self.players:
                turn = Turn()
                lockedDice = player.takeTurn(turn)
                
                if not turn.result:
                    print("Player {0} striked out".format(player))
                    continue
                
                value = Game.valueOf(lockedDice)
                if value == 0:
                    print("Player {0} didn't lock any dice".format(player))
                
                turn.score += value

    @staticmethod
    def valueOf(diceList):
        sortedDice = sorted([d.value for d in diceList])
        counter = collections.Counter(sortedDice)
        if len(sortedDice) == 6:
            if len(counter) == 6: # straight
                return 1500
            if max(counter.values()) == 2 and min(counter.values()) == 2: # three pairs
                return 2000
        sum = 0
        for n,c in counter.most_common():
            val = 0
            if c >= 3:
                if n == 1:
                    n = 10
                val = (n * 100) * pow(2, c - 3)
            elif n == 1:
                val = c * 100
            elif n == 5:
                val = c * 50
            sum += val
        return sum


class AIPlayer:
    def __init__(self):
        pass
    
    def takeTurn(self, turn):
        result = turn.take()
        print("Taking turn:")
        print("  Got:       {0}".format(turn.dice))
        print("  Result:    {0}".format(result))
        print("  Value:     {0}".format(Game.valueOf(turn.dice)))
        
        return []
        

game = Game()
game.addPlayer(AIPlayer())
game.run()


