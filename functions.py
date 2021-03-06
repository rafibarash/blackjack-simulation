from person import *


def initialize_player_dealer(game):
    '''initialize player/dealer'''
    num_of_players = game.getNumOfPlayers()
    for i in range(num_of_players):  # loop initializes each player
        p = Player()
        print("Initializing Player" + str(i))
        game.addPlayer(p)  # adds player to game list
    dealer = Dealer()  # initializes dealer
    game.setDealer(dealer)
    print("Initializing Dealer")
    print("")


def ask_for_bet(game):
    '''asks each player for a bet'''
    num_of_players = game.getNumOfPlayers()
    for i in range(num_of_players):  # loop asking each player for bets
        bet = int(input("player" + str(i) + ", enter your bet: "))
        player = game.getPlayer(i)
        player.setBet(bet)
        game.updatePlayer(player, i)


def give_player_dealer_hand(game, deck):
    '''gives player and dealer a hand'''
    num_of_players = game.getNumOfPlayers()
    for i in range(num_of_players):  # give each player initial hand
        p = game.getPlayer(i)
        p.clearHand()
        p.clearSplitHand()
        for j in range(2):  # loop gives player two cards from deck
            card = deck.pop()
            p.addCard(card)
        game.updatePlayer(p, i)  # updates player in game's player list
    dealer = game.getDealer()
    dealer.clearHand()
    for i in range(2):  # give dealer initial hand
        card = deck.pop()
        dealer.addCard(card)
    game.setDealer(dealer)  # sets dealer in game class


def play_blackjack(game, deck):
    '''runs blackjack simulation for each player'''
    dealer = game.getDealer()  # get dealer
    dhand = dealer.getHand()  # get dealer's hand
    num_of_players = game.getNumOfPlayers()  # get player list
    print("The Dealer's first card is: " + dhand[0])
    for i in range(num_of_players):  # loop for each player
        p = game.getPlayer(i)  # get's player
        if p.money < 0:
            print("Sorry player" + str(i) + ", you have a negative balance. Bye bitch.")
            game.deletePlayer(i)
            num_of_players = game.getNumOfPlayers()  # get player list
        else:
            print("")
            print("Player" + str(i) + "'s turn: ")
            p.play(i, deck)  # Player plays his turn
            game.updatePlayer(p, i)  # updates player in game's player list
    print("")
    dealer.playTurn(deck)  # dealer's turn
    dhand = dealer.getHand()  # gets dealer's new hand
    dhand_value = dealer.highestScore()  # gets value of dealer's new hand
    print("The dealer's hand is " + dhand)
    print("The dealer's hand value is: " + str(dhand_value))
    for i in range(num_of_players):  # loop to see who won
        p = game.getPlayer(i)
        phand_value = p.highestScore()

        split = p.checkSplit()  # checks to see if player split
        if split == "false":  # player did not split
            print("")
            print("Player" + str(i) + "'s hand value is: " + str(phand_value))
            print("The dealer's hand value is: " + str(dhand_value))
            game.winner(p, phand_value, dhand_value, i)  # decides winner of player vs dealer
        else:  # player split
            print("")
            print("Player" + str(i) + "'s first hand value is: " + str(phand_value))
            print("The dealer's hand value is: " + str(dhand_value))
            game.winner(p, phand_value, dhand_value, i)  # decides winner of first hand

            p_split_value = p.splitHighestScore()
            print("Player" + str(i) + "'s second hand value is: " + str(p_split_value))
            print("The dealer's hand value is: " + str(dhand_value))
            game.winner(p, p_split_value, dhand_value, i)  # decides winner of second hand
