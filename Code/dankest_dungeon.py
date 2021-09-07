#!/usr/local/bin/python
#Author: Erik Sandberg Co-author: Dalton Simac
import numpy as np
import sys
import time
import os
from dungeon_classes import *
from dungeon_functions import *
from dankest_storyline import *


# define character attributes
starting_level = 1
start_health = 100
start_damage = 1
start_defense = 1
start_money = 0
start_potions = 1
first_floor = 1
start_score=0
start_exp=0
start_maxexp=10
start_keys = 0
try:
    local_high_score = int(np.loadtxt('local_high_score.txt'))
except:
    local_high_score = 0
    
# combine into one array for simplicity
character_starting_values = [starting_level,start_health,start_damage,start_defense, start_money, start_potions,first_floor,start_score,start_exp,start_maxexp,start_keys]


# define floor attributes
gridsize_x = np.random.randint(3,8)
gridsize_y = np.random.randint(3,8)
dimensions = [gridsize_x,gridsize_y]
starting_position = [np.random.randint(gridsize_x),np.random.randint(gridsize_y)]
player_position = starting_position
starting_stairs = [np.random.randint(gridsize_x),np.random.randint(gridsize_y)]
while starting_stairs == player_position:
    starting_stairs = [np.random.randint(gridsize_x),np.random.randint(gridsize_y)]


floor_starting_values = [gridsize_x,gridsize_y, np.random.randint(min(dimensions),max(dimensions)*2), [], starting_position, starting_position, [], starting_stairs]
floor = Floor(*floor_starting_values)
floor.generate_monsters()

outdoors = Outdoors()
haybail = Haybail()


#Initialize the game
intro()

user = player(*load_character(character_starting_values))

user.local_high_score = local_high_score
clear()
#user.archery=True # for testing
#user.in_dungeon = False # For testing
#user.outside = False # for testing

while user.in_dungeon: # dungeon sequence
    clear()
    move_player(floor,user)
outside_intro()
while user.outside: # outdoor sequence
    clear()
    running(outdoors,user)
archery_intro()    

show_target(user,haybail)
# got past the haybail
clear()
print('YOU ARE THE HAYBAIL CHAMP!')
time.sleep(3)
if user.haybailchamp:
    #clear()
    print('GAME OVER')
    time.sleep(3)
    #running(user,outdoors)

