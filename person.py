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
    def getHighestScore(self):
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
    def isThereBlackjack(self):
        '''checks to see if there is a blackjack'''
        if self.getHighestScore == 21:
            return True
        else:
            return False

class Player(Person):
    def __init__(self):
        super().__init__(hand)
    def 
        

class Dealer(Person):
    def __init__(self):
        super().__init__(hand)
