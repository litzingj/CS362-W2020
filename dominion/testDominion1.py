# -*- coding: utf-8 -*-
"""
Date: 1/16/20

@author: Jaelyn Litzinger
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names
player_names = testUtility.getPlayerNames();

# number of curses and victory cards
nV = testUtility.setNumVictory(player_names);
nC = testUtility.setNumCurse(player_names);

# Define box and supply order
box = testUtility.makeBox(nV);

supply_order = testUtility.setSupplyOrder();

# Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list, [(k, box[k]) for k in random10])

# The supply always has these cards
player_names = ["Jenny", "Lenny"];
supply = testUtility.addSupplyDefaults(supply, nV, nC, player_names);

# initialize the trash
trash = []

# Costruct the Player objects
players = testUtility.makePlayers(player_names);

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
