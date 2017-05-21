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
        self.dealer = None
    def setDealer(self,dealer):
        self.dealer = dealer
    def getDealer(self):
        return self.dealer
    def addPlayer(self,player):
        self.players += [player]
    def updatePlayer(self,player,index):
        self.players[index] = player
    def getPlayer(self,index):
        return self.players[index]
    def updatePlayerList(self,newPlayerList):
        self.players = newPlayerList
    def getPlayerList(self):
        return self.players
    def winner(self,player,dealer):
        pvalue = player.highestScore()
        dvalue = dealer.highestScore()
        if pvalue > dvalue: #player wins
            print(p+" wins!")
            bet = p.getBet()
            p.addMoney(bet)
            new_money = p.getMoney()
            print(p+" has a balance of $"+str(new_money))
        elif dvalue > pvalue: #dealer wins
            print(p+" loses :(")
            bet = p.getBet()
            p.addMoney(bet)
            new_money = p.getMoney()
            print(p+" has a balance of $"+str(new_money))
        else:#tie
            print(p+" ties.")
            print(p+" has a balance of $"+str(new_money))

class Deck():
    def __init__(self):
        self.deck = []
    def resetDeck(self,num):
        cardsList = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        for ch in cardsList:
            for i in range(num):
                self.deck += [ch]
    def shuffle(self):
        random.shuffle(self.deck)
    def getDeck(self):
        return self.deck
    def pop(self):
        if len(self.deck) < 30:
            self.resetDeck(6)
            (self.deck).pop()
        else:
            return (self.deck).pop()
