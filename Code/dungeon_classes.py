#!/usr/local/bin/python
#Erik Sandberg
#Classes used in dankest_dungeon.py
import numpy as np
import sys
import time
import os


class player():
    def __init__(self,level,health,damage,defense,money,health_potions,floor,score,exp,maxexp,keys):
        self.level=level
        self.health=health
        self.damage=damage
        self.defense=defense
        self.money=money
        self.health_potions = health_potions
        self.floor=floor
        self.monster_counter = 0
        self.score = score
        self.exp = exp
        self.maxexp = maxexp # exp needed to level up
        self.keys = keys
        self.local_high_score = 0
        self.in_dungeon = True
        self.outside = False
        self.superboots = False
        self.archery = False
        self.haybailchamp = False
        self.aimer = [np.random.randint(-3,4),3+np.random.randint(-3,4)]

    def gain_exp(self,value):
        self.exp += value
        print('You gained ' + str(value) + ' experience.')
        if self.exp >= self.maxexp:
            self.level_up()
            self.exp = self.exp%self.maxexp
            self.maxexp += 5
        print(str(self.maxexp - self.exp) + ' more experience to level up!')
        
    def lose_health(self,loss_of_health):
        if self.defense >= loss_of_health:
            return
        self.health -= (loss_of_health-self.defense)
        print('You lost ' + str(loss_of_health-self.defense) + ' health. ')
        
    def gain_health(self,gain_of_health):
        self.health += gain_of_health
        if self.health >= 100:
            print('You are at max health!')
            time.sleep(2)
            self.health = 100
            print('You healed for ' + str(100-gain_of_health))
            return
        else:
            print('You healed for ' + str(gain_of_health))
        print('Current health is now '+ str(self.health))

    def gain_money(self,gain_of_money):
        self.money += gain_of_money
    def lose_money(self,loss_of_money):
        self.money -= loss_of_money
    def lose_health_potion(self,number):
        self.health_potions -= number
        print('You have ' + str(self.health_potions) + ' health potions left.')
        time.sleep(2)
    def level_up(self):
        self.level += 1
        self.damage +=1
        self.defense +=1
        self.add_score(100) # level gives 100 points
        print('You reached level ', str(self.level) + '! You have grown in strength.')
        time.sleep(2)
    def defeat_monster(self,value):
        self.monster_counter +=1
        self.gain_exp(value)
        
    def add_score(self,points):
        self.score += points

class Haybail():
    def __init__(self):
        self.name = 'Haybail'
        self.health = 100
    def lose_health(self,num):
        self.health -= num
        if self.health > 0:
            print('Haybail has '+ str(self.health) + ' health remaining.')
        else:
            print('Haybail has been defeated. ')
            
class Floor():
    def __init__(self,gridsize_x,gridsize_y,number_of_monsters,monster_positions,starting_position,player_position, sensei_position,stair_position):
        self.gridsize_x = gridsize_x
        self.gridsize_y = gridsize_y
        self.dimensions = [gridsize_x,gridsize_y]
        self.number_of_monsters = number_of_monsters
        self.monster_positions = monster_positions
        self.starting_position = starting_position
        self.player_position = player_position
        self.sensei_position = sensei_position
        self.stair_position = stair_position
        self.monster_list = [[5,2,'Blob',1,2,3],[12,4,'Giant spider',3,10,10],[10,3,'Zombie',2,5,6],[1,1,'Bat',1,1,2],[25,10,'Guard',10,200,30]]
        self.door_position = []

        

    def generate_monsters(self):
        for i in range(self.number_of_monsters):
            self.monster_positions.append([np.random.randint(self.gridsize_x),np.random.randint(self.gridsize_y)])


class monster():
    def __init__(self,health,damage,name,value,score,experience):
        self.health = health
        self.damage = damage
        self.name = name
        self.value = value
        self.score = score
        self.experience = experience
        
    def lose_health(self,loss_of_health):
        self.health -= loss_of_health
        

class Sensei():
    def __init__(self,available_health_potions,teach_offense, teach_defense):
        self.available_health_potions = available_health_potions
        self.teach_offense = teach_offense
        self.teach_defense = teach_defense

    def lose_health_potion(self,user):
        if user.money < 1:
            print('You do not have enough money. ')
            return
        if self.available_health_potions > 0:
            user.health_potions +=1
            user.money -= 1 # cost of potion
            print('You now have ' + str(user.health_potions) + ' health potions. May they serve you well, adventurer. ')
        else:
            print('I have no more potions for you, small grasshopper. ')
        self.available_health_potions -= 1
        

    def lose_teach_offense(self,user):
        if user.money < 2:
            print('You do not have enough money. ')
            return
        if self.teach_offense > 0:
            user.damage += 1
            user.money -= 2 # cost of learning
            print('You learn quickly. Your damage is now ' + str(user.damage) + '.')
        else:
            print('You have gained all of my offensive knowledge. ')
        self.teach_offense -= 1

    def lose_teach_defense(self,user):
        if user.money < 2:
            print('You do not have enough money. ')
            return
        if self.teach_defense > 0:
            user.defense += 1
            user.money -= 2 # cost of learning
            print('Well done, light mongoose. You now have ' + str(user.defense) + ' defense. ')
        else:
            print('You have already learned more defensive tactics than I, young master. ')
            self.teach_defense -= 1


class Outdoors():
    def __init__(self):
        self.gridsize_x = 10
        self.gridsize_y = 5
        self.player_position = [0,0]
        self.obstacle_locations = [] 
        self.item_locations = []


    def generate(self,number_obstacles,number_items): # obstacles start at x=gridsize_x and work their way left
        for i in range(number_obstacles):
            self.obstacle_locations.append([self.gridsize_x-1,np.random.randint(0,self.gridsize_y)])
            if len(self.obstacle_locations) > 1:
                while self.obstacle_locations[-1] in self.obstacle_locations[:-1]: #ensure no duplicate occupancy
                    del(self.obstacle_locations[-1])
                    self.obstacle_locations.append([self.gridsize_x-1,np.random.randint(0,self.gridsize_y)])
        for i in range(number_items):
            self.item_locations.append([self.gridsize_x-1,np.random.randint(0,self.gridsize_y)])
            while self.item_locations[-1] in self.obstacle_locations: #only works for 1 item, 1 obst
                del(self.item_locations[-1])
                self.item_locations.append([self.gridsize_x-1,np.random.randint(0,self.gridsize_y)])
                
    def advance_terrain(self,number_obstacles,number_items):
#        self.generate(number_obstacles,number_items)

        for obstacle_counter, position in enumerate(self.obstacle_locations):
            if position[0] < 1: # ZERO OR ONE
                del(self.obstacle_locations[obstacle_counter])
            try:
                self.obstacle_locations[obstacle_counter][0] -= 1
            except:
                pass
        for item_counter, position in enumerate(self.item_locations):
            if position[0] < 1: # ZERO OR ONE
                del(self.item_locations[item_counter])
            try:
                self.item_locations[item_counter][0] -= 1
            except:
                pass                
        self.generate(number_obstacles,number_items)

        
#class Target():
 #   def __init__(self):
  #      self.gridsize_x = 
