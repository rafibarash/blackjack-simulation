#need game class
    #isThereWinner method with player/dealer input to determine if winner. Also removes player from "players" list
    #stillPlaying method, returns True/False if players still in game
#need a deck class
    #input x amount of decks
    #shuffle method
    #getNumberOfCards method
    #giveCard method (use .pop)

import random

class Game():
    def __init__(self):
        self.players = []
    def addPlayer(self,player):
        self.players += [player]
    def getPlayerList(self):
        return self.players
    def getPlayer(self,index):
        return self.players[index]
    def removePlayer(self,index):
        del self.players[index]
    def updatePlayer(self,player,index):
        self.players[index] = player
        
class Deck():
    def __init__(self):
        self.theDeck
    def shuffled(self,num_of_decks)
        a = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']
        b = []
        for i in a:
            b.extend([i]*num_of_decks) #create
        random.shuffle(b)
        return b
