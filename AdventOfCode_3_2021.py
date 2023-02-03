#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:32:27 2022

@author: chloe
"""


########################################################################
# Imports
########################################################################
import re


########################################################################
# Fonctions
########################################################################
def liste_binaires(x):
    """ this function produces from a list of position, a list of list of position 
    input : list of position
    output: list of list of position"""
    # Initialisation
    liste_binaire=[]
    pos = []
    
    # Keep all the moves in lists containing direction and value of the move
    for line in x:
        pos = re.split(' |\n', line)
        liste_binaire.append(pos[:1])
        
    return liste_binaire


def obtain_gamma_epsilon_binary(x):
    """ this function allows to obtain gamma by finding the consensus sequence: 
        for each position keep the value the most represented.
        input : a list of binary sequences
        output : one binary sequence"""
    
    #Initialisation : 
    gamma =[]
    epsilon=[]
    c={}
    z={}

    
    ## Initialiser les clés des dictionnaires
    for elem in x:
        compteur =0
        for n in elem: 
            c[compteur]=0
            z[compteur]=0
            compteur +=1
          
    # Compter les 1 et les 0 pour savoir lequel est le plus grand des deux   
    for elem in x: 
        compteur=0
        for n in elem :
            if n == "1" :
               
                c[compteur] += 1
            elif n == "0" :
               
                z[compteur] += 1
            compteur +=1
        
    
    # Comparer les valeurs de zero et de 1 pour chaque position et déterminer si c'est epsilon ou gamma
    
    i =0
    while i < len(c):
        if c[i]< z[i]:
            gamma.append(0)
            epsilon.append(1)
        elif c[i] > z[i]:
            gamma.append(1)
            epsilon.append(0)
        i+=1
        
    return (gamma, epsilon)
    

        

def binary_to_decimal(binary):
    """ this function takes a binary number (contains only 0 and 1) and 
    converts it into decimal.
    input : binary number as a list of 0 and 1
    output : decimal number"""
    decimal =0
    i=0
    puissance = 0
    while i< len(binary):
        puissance = len(binary)-(i+1)
        decimal += binary[i]*pow(2,puissance)
        i+=1
        
    return(decimal)
    




########################################################################
#  Main
########################################################################


# Open the file
f = open(file ="/home/chloe/Téléchargements/input_day3.txt")
matrix =f.readlines()


# Day 1 - Part 1

gamma = obtain_gamma_epsilon_binary(matrix)[0]
epsilon = obtain_gamma_epsilon_binary(matrix)[1]
gamma_decimal = binary_to_decimal(gamma)
epsilon_decimal = binary_to_decimal(epsilon)
print(gamma_decimal*epsilon_decimal)




# Day 2 - Part 2
#print(aim_position(matrix))