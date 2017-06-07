import random

class Game():
    def __init__(self):
        self.players = []
        self.dealer = None
        self.num_of_players = 0
    def setDealer(self,dealer):
        '''sets dealer'''
        self.dealer = dealer
    def getDealer(self):
        '''returns dealer'''
        return self.dealer
    def addPlayer(self,player):
        '''adds player to player list'''
        self.players += [player]
    def updatePlayer(self,player,index):
        '''updates player in player list'''
        self.players[index] = player
    def getPlayer(self,index):
        '''returns a player in player list'''
        return self.players[index]
    def updatePlayerList(self,newPlayerList):
        '''replaces player list'''
        self.players = newPlayerList
    def getPlayerList(self):
        '''returns player list'''
        return self.players
    def setNumOfPlayers(self,num):
        '''number of players in game'''
        self.num_of_players = num
    def getNumOfPlayers(self):
        '''returns number of players'''
        return self.num_of_players
    def winner(self,player,dealer,index):
        '''checks winner of a player vs dealer'''
        pvalue = player.highestScore() #highest score of player
        dvalue = dealer.highestScore() #highest score of dealer
        if pvalue > dvalue and pvalue <= 21: #player wins
            print("Player"+str(index)+" wins!")
            bet = player.getBet()
            player.addMoney(bet) #adds bet to player's account
        elif dvalue > pvalue and dvalue <= 21: #dealer wins
            print("Player"+str(index)+" loses :(")
            bet = player.getBet()
            player.subMoney(bet) #subtracts bet from player's account
        elif pvalue == dvalue and pvalue <= 21 and dvalue <= 21: #tie
            print("Player"+str(index)+" ties.")
        else: #bust
            if pvalue <= 21 and dvalue > 21: #dealer busts and player doesn't
                print("Dealer busts. Player"+str(index)+" wins!")
                bet = player.getBet()
                player.addMoney(bet) #adds bet to player's account
            else: #player busts
                print("Player"+str(index)+" busts. Dealer wins :(")
                bet = player.getBet()
                player.subMoney(bet) #subtracts bet from player's account
             
class Deck():
    def __init__(self):
        self.deck = []
    def resetDeck(self,num):
        '''creates pile of decks'''
        cardsList = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        self.deck = []
        for ch in cardsList:
            for i in range(num):
                self.deck += [ch]
    def shuffle(self):
        '''shuffles deck'''
        print("Shuffling deck...")
        random.shuffle(self.deck)
    def getDeck(self):
        '''returns deck'''
        return self.deck
    def pop(self):
        '''pops a card from deck'''
        if len(self.deck) < 30:
            self.resetDeck(6)
            self.shuffle()
            (self.deck).pop()
        else:
            return (self.deck).pop()
