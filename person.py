#need a person class
    #startHand method that starts person with two cards
    #hand attribute
    #blackjack method to check if cards equal 21
    #hit method to append card to end of hand
#need a dealer to inherit person
    #show initialization of dealer
    #showHand method to show all cards but first card
#need a player class to inherit person
    #input x amount of players to inherit person
    #show initialization of each player
    #money attribute
    #bet method
    #doubleDown method
    #split method
    #stay method to compare against dealer at end of turn

class Person():
    def __init__(self):
        self.hand = ''
    def highestScore(self):
        '''given string of cards, returns highest blackjack score if doesn't bust'''
        score = 0
        for ch in self.hand:
            if ch == 'T':
                score += 10
            elif ch == 'J':
                score += 10
            elif ch == 'Q':
                score += 10
            elif ch == 'K':
                score += 10
            elif ch == 'A':
                score += 11
            else:
                score += int(ch)
        aces = (self.hand).count('A')
        while score > 21 and aces != 0:
            score -= 10
            aces -= 1
        return score
    def addCard(self,card):
        self.hand += str(card)
    def clearHand(self):
        self.hand = ''
    def getHand(self):
        return self.hand

class Player(Person):
    def __init__(self,money=1000):
        self.bet = 0
        self.money = money
        self.blackjack = False
        self.hand = ''
        super().__init__()
    def setBet(self,bet):
        self.bet = bet
    def getBet(self):
        return self.bet
    def addMoney(self,money):
        self.money += money
    def subMoney(self,money):
        self.money -= money
    def getMoney(self):
        return self.money
    def hit(self):
        pass
    def doubleDown(self):
        pass
    def split(self):
        pass
    def blackjack(self,val):
        self.blackjack = val
    def play(self,i,deck):
        '''plays all turns for one player'''
        turn = 0
        endTurn = False
        while endTurn is False: #loop for each player turn
            hand = self.getHand()
            handValue = self.highestScore()
            if turn == 0:
                if handValue == 21:
                    self.blackjack = True
                    print("Player"+str(i)+", your hand is: "+hand[0]+', '+hand[1])
                    print("You have a blackjack!")
                    endTurn = True
            split = False
            if (handValue < 21) and (endTurn is False) and (split is False): #play turn
                print("Player"+str(i)+", your hand is: "+hand[0]+', '+hand[1])
                print("Player"+str(i)+", your hand value is: "+str(handValue))
                #decide whether to hit/stay/double/split
                decision = str(input("Will you hit, stay, double, or split? (please enter exact word): "))
                if decision == "hit":
                    self.hit()
                elif decision == "double":
                    self.doubleDown()
                    endTurn = True
                elif decision == "split":
                    self.split()
                    split = True
                else:
                    endTurn = True
            if split is True:
                for j in range(2):
                    split_finished = False
                    while not split_finished:
                        pass
            turn += 1

class Dealer(Person):
    def __init__(self):
        self.hand = ''
        super().__init__()
    def playTurn(self,deck):
        while True:
            if self.highestScore() >= 17:
                return False
            else:
                card = deck.pop()
                self.addCard(card)
                dhand = self.getHand()
                print("Dealer picks card...")
