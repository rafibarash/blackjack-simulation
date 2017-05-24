import random

class Game():
    def __init__(self):
        self.players = []
        self.dealer = None
        self.num_of_players = 0
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
    def setNumOfPlayers(self,num):
        self.num_of_players = num
    def getNumOfPlayers(self):
        return self.num_of_players
    def winner(self,player,dealer,index):
        pvalue = player.highestScore()
        dvalue = dealer.highestScore()
        if pvalue > dvalue and pvalue <= 21: #player wins
            print("Player"+str(index)+" wins!")
            bet = player.getBet()
            player.addMoney(bet)
            new_money = player.getMoney()
            print("Player"+str(index)+" has a balance of $"+str(new_money))
        elif dvalue > pvalue and dvalue <= 21: #dealer wins
            print("Player"+str(index)+" loses :(")
            bet = player.getBet()
            player.subMoney(bet)
            new_money = player.getMoney()
            print("Player"+str(index)+" has a balance of $"+str(new_money))
        elif pvalue == dvalue and pvalue <= 21 and dvalue <= 21: #tie
            new_money = player.getMoney()
            print("Player"+str(index)+" ties.")
            print("Player"+str(index)+" has a balance of $"+str(new_money))
        else: #bust
            if pvalue <= 21 and dvalue > 21: #dealer busts and player doesn't
                print("Dealer busts. Player"+str(index)+" wins!")
                bet = player.getBet()
                player.addMoney(bet)
                new_money = player.getMoney()
                print("Player"+str(index)+" has a balance of $"+str(new_money))
            else: #player busts
                print("Player"+str(index)+" busts. Dealer wins :(")
                bet = player.getBet()
                player.subMoney(bet)
                new_money = player.getMoney()
                print("Player"+str(index)+" has a balance of $"+str(new_money))
             
class Deck():
    def __init__(self):
        self.deck = []
    def resetDeck(self,num):
        cardsList = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        for ch in cardsList:
            for i in range(num):
                self.deck += [ch]
    def shuffle(self):
        print("Shuffling deck...")
        random.shuffle(self.deck)
    def getDeck(self):
        return self.deck
    def pop(self):
        if len(self.deck) < 30:
            self.resetDeck(6)
            self.shuffle()
            (self.deck).pop()
        else:
            return (self.deck).pop()
