#have all in method
#have method that kicks lo$$ers out of game
#also take out any characters that aren't numbers for bet

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
    def __init__(self):
        self.bet = 0
        self.split_bet = 0
        self.money = 1000
        self.blackjack = False
        self.hand = ''
        self.split_hand = ''
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
    def hit(self,deck):
        card = deck.pop()
        self.addCard(card)
    def doubleDown(self,deck):
        if self.hand[0]:
            self.bet *= 2
            card = deck.pop()
            self.addCard(card)
    def split(self,deck):
        if self.hand[0] == self.hand[1]:
            self.split_hand = (self.hand).pop()
            self.split_bet = self.bet
            return True
        else:
            return False
    def getSplitHand(self):
        return self.split_hand
    def splitHighestScore(self):
        '''given string of cards, returns highest blackjack score if doesn't bust'''
        score = 0
        for ch in self.split_hand:
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
        aces = (self.split_hand).count('A')
        while score > 21 and aces != 0:
            score -= 10
            aces -= 1
        return score
    def clearSplitHand(self):
        pass
    def splitHit(self,deck):
        card = deck.pop()
        self.split_hand += card
    def blackjack(self,val):
        self.blackjack = val
    def play(self,i,deck):
        '''plays all turns for one player'''
        turn = 0
        endTurn = False
        split = False
        while endTurn is False: #loop for each player turn
            hand = self.getHand()
            handValue = self.highestScore()
            if turn == 0 and handValue == 21:
                self.blackjack = True
                print("Player"+str(i)+", your hand is: "+hand[0]+', '+hand[1])
                print("You have a blackjack!")
                endTurn = True
            elif (handValue <= 21) and (endTurn is False) and (split is False): #play turn
                #decide whether to hit/stay/double/split
                print("Player"+str(i)+", your hand is: "+hand)
                print("Player"+str(i)+", your hand value is: "+str(handValue))    
                decision = str(input("Will you hit, stay, double, or split? (please enter exact word): "))
                if decision == "hit":
                    self.hit(deck)
                elif decision == "double":
                    self.doubleDown(deck)
                    endTurn = True
                elif decision == "split":
                    success_split = self.split(deck)
                    if success_split is True:
                        split = True
                    else:
                        print("You are not able to split with this hand")
                else:
                    endTurn = True
            elif split is True:
                original_finished = False
                while not original_finished:
                    hand = self.getHand()
                    handValue = self.highestScore()
                    if handValue <= 21:
                        print("Player"+str(i)+", your first hand is: "+hand)
                        print("Player"+str(i)+", your first hand value is: "+str(handValue))
                        decision = str(input("Will you hit or stay? (please enter exact word): "))
                        if decision == "hit":
                            self.hit(deck)
                        else: #stay
                            original_finished = True
                    else: #bust
                        print("Player"+str(i)+", your first hand has busted.")
                        original_finished = True                      
                split_finished = False
                while not split_finished:
                    hand = self.getSplitHand()
                    handValue = self.splitHighestScore()
                    if handValue <= 21:
                        print("Player"+str(i)+", your second hand is: "+hand)
                        print("Player"+str(i)+", your second hand value is: "+str(handValue))
                        decision = str(input("Will you hit or stay? (please enter exact word): "))
                        if decision == "hit":
                            self.splitHit(deck)
                        else: #stay
                            split_finished = True
                    else: #bust
                        print("Player"+str(i)+", your second hand has busted.")
                        split_finished = True                      
            else: #bust
                endTurn = True
                print("Player"+str(i)+", your hand is: "+hand)
                print("Player"+str(i)+", your hand value is: "+str(handValue))
                print("Player"+str(i)+", you have busted :(")
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
