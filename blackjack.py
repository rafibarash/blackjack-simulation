#how game works
#each player bets
#then each player and dealer gets two cards, dealer has one card showing
#before turns start, check to see if any players have natural blackjack
        #whenever player has blackjack and dealer does not, player receives 1.5x amt he gave
        #if both player and dealer have blackjack, player receives 1x amt he gave
#then loop of each player continuing his turn.
        #Stay, hit, split (if two cards are the same, only one extra card if spliting aces), or double (place second bet equal to first bet, player gets one more card).
        #when turn done, dealer adds cards until total => 17
#after round is over, update player list
                
#still need to do.
    #write method for hit
    #write method for double
    #write method for split
    #write loop for split==True in 'play' method

from game import *
from person import *

def initialize_player_dealer(game,num_of_players):
    '''initialize player/dealer'''
    for i in range(num_of_players): #loop initializes each player
        p = "player"+str(i)
        p = Player()
        print("Initializing Player"+str(i))
        game.addPlayer(p) #adds player to game list
    dealer = Dealer() #initializes dealer
    game.setDealer(dealer)
    print("Initializing Dealer")

def ask_for_bet(game,num_of_players):
    '''asks each player for a bet'''
    for i in range(num_of_players): #loop asking each player for bets
        bet = int(input("player"+str(i)+", enter your bet: "))
        player = game.getPlayer(i)
        player.setBet(bet)
        game.updatePlayer(player,i)

def give_player_dealer_hand(game,deck,num_of_players):
    '''gives player and dealer a hand'''
    #give player initial hand
    for i in range(num_of_players):
        p = game.getPlayer(i)
        for j in range(2): #loop gives player two cards from deck
            card = deck.pop()
            (p).addCard(card)
        game.updatePlayer(p,i)
    #give dealer initial hand
    dealer = game.getDealer()
    for i in range(2):
        card = deck.pop()
        dealer.addCard(card)
    game.setDealer(dealer)

def play_blackjack(game):
    dealer = game.getDealer
    dhand = dealer.getHand()
    print("The Dealer's first card is: "+dhand[0])
    for i in range(num_of_players): #loop for each player
        p = "player"+str(i)
        print(p+"'s turn: ")
        p.play(i) #Player plays his turn
    dealer.playTurn() #dealer's turn
    dhand_value = dealer.highestScore() #value of dealer's hand
    print("The dealer's hand value is: "+str(dhand_value))
    for i in range(num_of_players): #loop to see who won
        p = "player"+str(i)
        phand_value = p.highestScore()
        print(p+"' hand value is: "+str(phand_value))
        game.winner(p,dealer) #Prints winners and new account value
        
def main():
    '''main function for simulating a game of blackjack'''
    game = Game()
    deck = Deck()
    deck.resetDeck(6)
    deck.shuffle()

    num_of_players = int(input("Enter number of players: ")) #variable, number of players
    
    initialize_player_dealer(game,num_of_players)

    ask_for_bet(game,num_of_players)

    give_player_dealer_hand(game,deck,num_of_players)

    #Loop to check if still playing
    done = False
    rounds = 0
    while not done:
        play = str(input("Would you like to play another round: (y/n)")) #check if playing another round
        if play == 'n': #don't play round
            done = True
        else: #play round
            print("Round "+str(rounds)+"...")
            play_blackjack(game) #play game
            for index in range(num_of_players): #loop to update game's player list
                p = "player"+str(i)
                game.updatePlayer(p,index)#updates game list
            rounds += 1
                     
main()           
