#have all in method
#have method that kicks lo$$ers out of game
#also take out any characters that aren't numbers for bet
#if you split aces, autimatically end turn

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
            elif ch.isdigit() is True:
                score += int(ch)
            else:
                pass
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
        self.money = 1000
        self.blackjack = False
        self.hand = ''
        self.split = False #for split hands...
        self.split_hand = '' #for split hands...
        self.split_bet = 0 #for split hands...
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
    def checkSplit(self):
        '''returns 1 if player split, 0 otherwise'''
        if self.split is True: #player split
            return "true"
        else: #player did not split
            return "false"
    def getSplitHand(self):
        '''returns player's split hand'''
        return self.split_hand
    def clearSplitHand(self):
        '''clears split hand'''
        self.split_hand = ''
    def splitHit(self,deck):
        '''hits deck for split hand'''
        card = deck.pop()
        self.split_hand += card
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
    def blackjack(self):
        '''returns blackjack value of player'''
        return self.blackjack
    def play(self,i,deck):
        '''plays all turns for one player'''
        turn = 0
        endTurn = False
        while endTurn is False: #loop for each player turn
            hand = self.getHand()
            handValue = self.highestScore()
            if turn == 0 and handValue == 21:
                #checks if player has a blackjack at beginning of turn
                self.blackjack = True
                print("Player"+str(i)+", your hand is: "+hand[0]+', '+hand[1])
                print("You have a blackjack!")
                endTurn = True
            elif (handValue <= 21) and (endTurn is False) and (self.split is False): #play turn
                #decide whether to hit/stay/double/split
                print("Player"+str(i)+", your hand is: "+hand)
                print("Player"+str(i)+", your hand value is: "+str(handValue))    
                decision = str(input("Will you hit, stay, double, or split? (please enter exact word): "))
                if decision == "hit": #hit
                    self.hit(deck)
                elif decision == "double": #double down
                    if turn == 0: #check to see if player can double down                      
                        self.doubleDown(deck)
                        hand = self.getHand()
                        handValue = self.highestScore()
                        print("Player"+str(i)+", your hand is: "+str(hand))
                        print("Player"+str(i)+", your hand value is: "+str(handValue))
                        endTurn = True
                    else: #if player can't double, repeat turn
                        print("You are not able to double down. It is not the first turn.")
                elif decision == "split": #split
                    if turn == 0 and hand[0] == hand[1]:
                        self.split = True
                    else:
                        print("You are not able to split with this hand.")
                else: #stay
                    endTurn = True
            elif self.split is True: #runs turn for both hands after a split
                old_hand = self.getHand()
                self.hand = old_hand[0] #starts off first hand
                self.split_hand = old_hand[1] #starts off split hand

                ### Loop to play for first hand
                first_hand_done = False
                while first_hand_done is False:
                    first_hand = self.getHand() #get first hand
                    first_hand_value = self.highestScore() #get first hand value
                    if first_hand_value <= 21: #play if didn't bust
                        print("Player"+str(i)+", your first hand is: "+first_hand)
                        print("Player"+str(i)+", your first hand value is: "+str(first_hand_value))
                        decision = str(input("Will you hit or stay? (please enter exact word): "))
                        if decision == "hit": #hit
                            self.hit(deck)
                        else: #stay
                            first_hand_done = True
                    else: #bust
                        print("Player"+str(i)+", your first hand is: "+first_hand)
                        print("Player"+str(i)+", your first hand value is: "+str(first_hand_value))
                        print("Player"+str(i)+", your first hand has busted. :(")
                        first_hand_done = True

                ### Loop to play for split hand
                split_hand_done = False
                while split_hand_done is False:
                    split_hand = self.getSplitHand() #get split hand
                    split_hand_value = self.splitHighestScore() #get split hand value
                    if split_hand_value <= 21: #play if didn't bust
                        print("Player"+str(i)+", your second hand is: "+split_hand)
                        print("Player"+str(i)+", your second hand value is: "+str(split_hand_value))
                        decision = str(input("Will you hit or stay? (please enter exact word): "))
                        if decision == "hit": #hit
                            self.splitHit(deck)
                        else: #stay
                            split_hand_done = True
                    else: #bust
                        print("Player"+str(i)+", your second hand has busted.")
                        split_hand_done = True
                endTurn = True #split turn is done
                
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
                print("Dealer picks card...")
