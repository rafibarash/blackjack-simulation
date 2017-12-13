# to do
# if blackjack win 1.5 amount of bet
# why does a None value pop up in the deck here and there
# make sure if money runs out player is out of game

from game import *
from person import *
from functions import *


def main():
    '''main function for simulating a game of blackjack'''
    game = Game()  # initialize game class
    deck = Deck()  # initialize deck
    deck.resetDeck(6)  # creates pile of 6 decks
    deck.shuffle()  # shuffles deck

    num_of_players = int(input("Enter number of players: "))  # number of players
    game.setNumOfPlayers(num_of_players)  # enters number of players in game

    initialize_player_dealer(game)  # initializes each player and dealer

    # Loop to check if still playing
    done = False
    rounds = 0
    while not done:
        if rounds > 0:
            play = str(input("Would you like to play another round (y/n): "))  # check if playing another round
        else:
            play = 'y'
        if play == 'n':  # don't play round
            done = True
        else:  # play round
            print('')
            print("Round " + str(rounds) + "...")
            give_player_dealer_hand(game, deck)  # gives hand to players and dealer
            playerList = game.getPlayerList()
            for i in range(num_of_players):  # tells each player his balance
                p = game.getPlayer(i)
                if p.money < 0:
                    print("Player" + str(i) + " has a balance of $" + str(playerList[i].getMoney()))
                    print("Sorry player" + str(i) + ", you have a negative balance. Bye bitch.")
                    game.deletePlayer(i)
                    num_of_players -= 1
                else:
                    print("Player" + str(i) + " has a balance of $" + str(playerList[i].getMoney()))
            ask_for_bet(game)  # asks each player for a bet
            play_blackjack(game, deck)  # play game
            rounds += 1  # end of round


main()
