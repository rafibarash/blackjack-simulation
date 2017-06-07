#have all in method
#have method that kicks lo$$ers out of game
#also take out any characters that aren't numbers for bet

class Person():
    def __init__(self):
        self.hand = ''
    def highestScore(self):
        '''returns person's best blackjack score'''
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
        '''adds card to person's hand'''
        self.hand += str(card)
    def clearHand(self):
        '''clears person's hand'''
        self.hand = ''
    def getHand(self):
        '''returns person's hand'''
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
        '''sets bet for current turn'''
        self.bet = bet
    def getBet(self):
        '''returns current bet'''
        return self.bet
    def addMoney(self,money):
        '''adds money to player's account'''
        self.money += money
    def subMoney(self,money):
        '''subtracts money from player's account'''
        self.money -= money
    def getMoney(self):
        '''returns money in player's account'''
        return self.money
    def hit(self,deck):
        '''pops card from deck and adds to player's hand'''
        card = deck.pop()
        self.addCard(card)
    def doubleDown(self,deck):
        '''hits deck and doubles bet'''
        if self.hand[0]:
            self.bet *= 2
            card = deck.pop()
            self.addCard(card)
    def split(self,deck):
        '''creates two hands for player'''
        if self.hand[0] == self.hand[1]:
            self.split_hand = (self.hand).pop()
            self.split_bet = self.bet
            return True
        else:
            return False
    def getSplitHand(self):
        '''returns player's split hand'''
        return self.split_hand
    def splitHighestScore(self):
        '''returns best blackjack score of split hand'''
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
        '''clears split hand'''
        self.split_hand = ''
    def splitHit(self,deck):
        '''hits deck for split hand'''
        card = deck.pop()
        self.split_hand += card
    def blackjack(self):
        '''returns blackjack value of player'''
        return self.blackjack
    def play(self,i,deck):
        '''plays all turns for one player'''
        turn = 0
        endTurn = False
        split = False
        while endTurn is False: #loop for each player turn
            hand = self.getHand()
            handValue = self.highestScore()
            if turn == 0 and handValue == 21:
                #checks if player has a blackjack at beginning of turn
                self.blackjack = True
                print("Player"+str(i)+", your hand is: "+hand[0]+', '+hand[1])
                print("You have a blackjack!")
                endTurn = True
            elif (handValue <= 21) and (endTurn is False) and (split is False): #play turn
                #decide whether to hit/stay/double/split
                print("Player"+str(i)+", your hand is: "+hand)
                print("Player"+str(i)+", your hand value is: "+str(handValue))    
                decision = str(input("Will you hit, stay, double, or split? (please enter exact word): "))
                if decision == "hit": #hit
                    self.hit(deck)
                elif decision == "double": #double down
                    self.doubleDown(deck)
                    hand = self.getHand()
                    handValue = self.highestScore()
                    print("Player"+str(i)+", your hand is: "+str(hand))
                    print("Player"+str(i)+", your hand value is: "+str(handValue))
                    endTurn = True
                elif decision == "split": #split
                    success_split = self.split(deck)
                    if success_split is True:
                        split = True
                    else:
                        print("You are not able to split with this hand")
                else: #stay
                    endTurn = True
            elif split is True: #runs turn for both hands after a split
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
        '''plays dealer's turn'''
        while True:
            if self.highestScore() >= 17: #stop turn if dealer's hand > 17
                return False
            else: #add card to dealer's hand
                card = deck.pop()
                self.addCard(card)
                dhand = self.getHand()
                print("Dealer picks card...")
