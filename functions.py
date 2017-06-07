from game import *
from person import *

def initialize_player_dealer(game):
    '''initialize player/dealer'''
    num_of_players = game.getNumOfPlayers()
    for i in range(num_of_players): #loop initializes each player
        p = "player"+str(i)
        p = Player()
        print("Initializing Player"+str(i))
        game.addPlayer(p) #adds player to game list
    dealer = Dealer() #initializes dealer
    game.setDealer(dealer)
    print("Initializing Dealer")
    print("")

def ask_for_bet(game):
    '''asks each player for a bet'''
    num_of_players = game.getNumOfPlayers()
    for i in range(num_of_players): #loop asking each player for bets
        bet = int(input("player"+str(i)+", enter your bet: "))
        player = game.getPlayer(i)
        player.setBet(bet)
        game.updatePlayer(player,i)

def give_player_dealer_hand(game,deck):
    '''gives player and dealer a hand'''
    num_of_players = game.getNumOfPlayers()
    for i in range(num_of_players): #give each player initial hand
        p = game.getPlayer(i)
        p.clearHand()
        for j in range(2): #loop gives player two cards from deck
            card = deck.pop()
            p.addCard(card)
        game.updatePlayer(p,i) #updates player in game's player list
    dealer = game.getDealer()
    dealer.clearHand()
    for i in range(2): #give dealer initial hand
        card = deck.pop()
        dealer.addCard(card)
    game.setDealer(dealer) #sets dealer in game class

def play_blackjack(game,deck):
    '''runs blackjack simulation for each player'''
    dealer = game.getDealer() #get dealer
    dhand = dealer.getHand() #get dealer's hand
    num_of_players = game.getNumOfPlayers() #get player list
    print("The Dealer's first card is: "+dhand[0])
    for i in range(num_of_players): #loop for each player
        p = game.getPlayer(i) #get's player
        print("")
        print("Player"+str(i)+"'s turn: ")
        p.play(i,deck) #Player plays his turn
        game.updatePlayer(p,i) #updates player in game's player list
    print("")
    dealer.playTurn(deck) #dealer's turn
    dhand = dealer.getHand() #gets dealer's new hand
    dhand_value = dealer.highestScore() #gets value of dealer's new hand
    print("The dealer's hand is "+dhand)
    print("The dealer's hand value is: "+str(dhand_value))
    for i in range(num_of_players): #loop to see who won
        p = game.getPlayer(i)
        phand_value = p.highestScore()
        print("")
        print("Player"+str(i)+"'s hand value is: "+str(phand_value))
        print("The dealer's hand value is: "+str(dhand_value))
        game.winner(p,dealer,i) #decides winner of player vs dealer
