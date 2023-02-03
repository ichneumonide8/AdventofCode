#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:22:26 2022

@author: chloe
"""

########################################################################
# Imports
########################################################################
import re

########################################################################
# Fonctions
########################################################################
# Day 2 - Part 1
def liste_positions(x):
    """ this function produces from a list of position, a list of list of position 
    input : list of position
    output: list of list of position"""
    # Initialisation
    liste_position=[]
    pos = []
    
    # Keep all the moves in lists containing direction and value of the move
    for line in x:
        pos = re.split(' |\n', line)
        liste_position.append(pos[:2])
    return liste_position


def position(x):
    """ this function find the position of the submarine and multiply horizontal and depth position
    input : a list of position
    output: an integer horizontal x depth position"""
    liste_position=liste_positions(x)
   
    
    
    # Initialisation
    horizontal =0
    depth = 0
    
    # for each element from our list of move, we update the horizontal or depth position 
    for elem in liste_position :
        if elem[0] == "forward" :
            horizontal+= int(elem[1])
        elif elem[0] == "up" :
            depth -= int(elem[1])
        elif elem[0] == "down" :
            depth += int(elem[1])
            
    m = horizontal * depth
    return m
  

def aim_position(x):
    """ this function find the position and the aim. it also multiply horizontal by depth
    input :   a list of position
    output : an integer horizontal * depth position that take into account the aim"""
    
    # Initialisation
    horizontal =0
    depth = 0
    aim = 0
    
    
    liste_position=liste_positions(x)
    for elem in liste_position :
        if elem[0] == "forward" :
            horizontal+= int(elem[1])
            depth += int(elem[1])*aim
        elif elem[0] == "up" :
            aim -= int(elem[1])
        elif elem[0] == "down" :
            aim += int(elem[1])
            
    m = horizontal * depth
    return m
    

########################################################################
#  Main
########################################################################


# Open the file
f = open(file ="/home/chloe/Téléchargements/input_day2.txt")
matrix =f.readlines()
#print(matrix)

# Day 1 - Part 1
print(position(matrix))




# Day 2 - Part 2
print(aim_position(matrix))