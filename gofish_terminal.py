# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 00:10:38 2026

@author: hasan
"""
import random
import time
from pprint import pprint
"""
Welcome to GoFish!
This is a game where you get what you want or go fricking fishing!
The rules are simple:
    Each player takes a turn, asking for a card in their hand from a random player.
    If that player has the card, they must give it to the person requested it.
    Successful players play again until they fail. When failed, they draw from the 
    draw pile and it is other player's turn.
    Game ends when there are no cards left in the middle and no player has any cards left.

    START GAME
"""

ranks = [str(rank) for rank in range(2, 11)] + ['J', 'Q', 'K', 'A']
suits = ['spades', 'diamonds', 'clubs', 'hearts']

deck = [(rank, suit) for suit in suits for rank in ranks]
shuffled = random.sample(deck, len(deck))

"""For player count 4 and less, 7 cards are recommended. For 4 and more, 5 cards are ideal."""
player_count = int(input("How many players? "))
players = [[] for _ in range(player_count)]
scores = [0 for _ in range(player_count)]
results = ""
cplayers = [[] for _ in range(player_count)]
card_count = int(input("How many cards for each hand? "))

for i in range(player_count):
    for j in range(card_count):
        players[i].append(shuffled[-1])
        shuffled.pop(-1)
#player decks are ready

for i in range(player_count):
    for j in range(card_count):
        cplayers[i].append(players[i][j][0]) 

while True:
    print("Game is starting... Deck is shuffling...")
    time.sleep(2)
    print("Dealing cards...")
    time.sleep(2)
    print("Cards are dealt to each player.")
    i = 0
    gameOver = 0
    while gameOver == 0:
        i = i % player_count
        print(f"Player {i} starts. Their hand: ")
        pprint(players[i])
        #their hand is displayed
        success_otherhand = 1
        while success_otherhand == 1:
            success_ownhand = 0 # this is if requested card is at self's hand
            while success_ownhand == 0:
                print(f"Player {i} takes action. Which rank do you request?")
                req_rank = input("Rank: ")
                if req_rank in cplayers[i]:
                    success_ownhand = 1
                else:
                    print(f"You don't have {req_rank} in your deck. Please try again. ")
            print("Alright.")
            success_otherplayer = 0 # this is if requested player is other or self
            while success_otherplayer == 0:       
                print(f"Player {i} takes action. Whom do you request from?")
                req_player = int(input("Player: "))
                print(i)
                if req_player != i:
                     success_otherplayer = 1
                else:
                    print("You have selected yourself. Please try another player.")
            
            if req_rank in cplayers[req_player]:
                success_otherhand = 1
                print("Yay they have the card you requested.")
                their_card = cplayers[req_player].index(req_rank)
                players[i].append(players[req_player][their_card])
                cplayers[i].append(cplayers[req_player][their_card])

                cplayers[req_player].pop(their_card) 
                players[req_player].pop(their_card)
                
                if cplayers[i].count(req_rank) == 4:
                    print(f"You have now collected all {req_rank}'s")
                    for k in range(4): # there are 4 suits
                        score_card = cplayers[i].index(req_rank)
                        cplayers[i].pop(score_card) 
                        players[i].pop(score_card)
                    scores[i] += 1
                    print(f"Current score for {'Player' + ' ' + str(i)}: {scores[i]}")

                print("It's your turn again.")
            else:
                if len(shuffled) > 0:   
                    players[i].append(shuffled[-1])
                    cplayers[i].append(players[i][-1][0]) 
                    print("Card was not found. A card is drawn into your hand and the next player takes their turn.")
                else:
                    print("Card was not found but also couldn't be drawn because deck is empty!")
                
                success_otherhand = 0
                i += 1

            # if not player3:
            #     gameOver = 1
            #     print("No player has any cards left. The game is over")
            if sum(scores) == 13:
                gameOver = 1
                print("No player has any cards left. The game is over")
    for r in range(player_count):
        results +=f"Score for Player {k}: {scores[i]}\n"
    print(results)
    break