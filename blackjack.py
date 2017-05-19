#how will i code this??
#need game class
    #isThereWinner method with player/dealer input to determine if winner. Also removes player from "players" list
    #stillPlaying method, returns True/False if players still in game
#need a deck class
    #input x amount of decks
    #shuffle method
    #getNumberOfCards method
    #giveCard method (use .pop)
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
    
from game import *
from person import *

def main():
    '''main function for simulating a game of blackjack'''
    game = Game()
    deck = Deck()
    deck.shuffle()
    
    #initialize each player and dealer
    num_of_players = int(input("Enter number of players: "))
    for i in range(num_of_players):
        ("player"+str(i)) = Person()
        ("player"+str(i)).
        game.addPlayer += ["player"+str(i)]
    dealer = Dealer()
    players = game.getPlayerList

    #give each player an initial hand
    for i in range(num_of_players):
        .startHand()
    dealer.startHand()
        
    #loop until there is a winner
    turns = 0
    while True:
        if turns == 0:
            for i in players: #does anyone have blackjack?
                game.isThereBlackjack(i,dealer)
        if game.stillPlaying() is True: #continue game
            dealer.showHand()
            #loop to decide whether to hit+continue or stay
            for i in players:
                decision = str(input("Will you hit, stay, double, or split? (please enter exact word)"))
                if decision == "hit":
                    i.hit()
                elif decision == "double":
                    i.doubleDown()
                elif decision == "split":
                    i.split()
                else:
                    i.stay()
            dealer.addCard
            #loop to see if any players stayed
            for i in players:
                if i.stay == True:
                    game.isThereWinner(i,dealer)
            turns += 1
        else: #stop game
            return False
            
            
                
        
    
    
