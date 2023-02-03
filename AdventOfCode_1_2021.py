#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:16:06 2022

@author: chloe
"""

########################################################################
# Imports
########################################################################

########################################################################
# Fonctions
########################################################################
# Day 1 - Part 1
def first_part(matrix):
    """ this function allows you to find out how many times a measurement is 
    higher than the previous measurement
    input : list of measurements
    output : number of increase"""
    # Initialisation
    c=0
    i=0
    while i < len(matrix)-1:
        if int(matrix[i])< int(matrix[i+1]):
            c+=1

        i+=1
     
    return c


def second_part(matrix):
    """This function counts the number of times the sum of measurements in this 
    sliding window increases from the previous sum. So, compare A with B,
    then compare B with C, then C with D, and so on. Stop when there aren't 
    enough measurements left to create a new three-measurement sum.
    input : list of measurements
    output : number of increase of the sum measurements"""
    
    #Initialisation
    l = 0
    m_sum = 0 
    L_m_sum =[]
    while l < len(matrix)-2:
        m_sum = int(matrix[l])+ int(matrix[l+1]) + int(matrix[l+2])
        L_m_sum.append(m_sum)
        #print(L_m_sum)
        l+=1
        
        
    
    return(first_part(L_m_sum))
    

########################################################################
#  Main
########################################################################


# Open the file
f = open(file ="/home/chloe/Téléchargements/input.txt")
matrix =f.readlines()


# Day 1 - Part 1
print("le nombre d'augmentation est", first_part(matrix))




# Day 2 - Part 2
print(second_part(matrix))
