#!/usr/bin/env python3
# coding=utf-8

"""
Not a lot going on here, this just holds the different races and variables for 
the ability modifiers that are added to the ability functions in char_sheet.py.

Brandon Cowan
"""

class Races():

    def dwarf():
        strength = 0
        constitution = 2
        dexterity = 0
        wisdom = 0
        intelligence = 0
        charisma = 0

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def elf():
        strength = 0
        constitution = 0
        dexterity = 2
        wisdom = 0
        intelligence = 0
        charisma = 0

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def halfling():
        strength = 0
        constitution = 0
        dexterity = 2
        wisdom = 0
        intelligence = 0
        charisma = 0

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def human():
        strength = 1
        constitution = 1
        dexterity = 1
        wisdom = 1
        intelligence = 1
        charisma = 1

        return strength, constitution, dexterity, wisdom, intelligence, charisma
    
    def dragonborn():
        strength = 0
        constitution = 0
        dexterity = 0
        wisdom = 0
        intelligence = 0
        charisma = 0

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def gnome():
        strength = 0
        constitution = 0
        dexterity = 0
        wisdom = 0
        intelligence = 2
        charisma = 0

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def half_elf():
        strength = 0
        constitution = 0
        dexterity = 0
        wisdom = 0
        intelligence = 0
        charisma = 2

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def half_orc():
        strength = 2
        constitution = 1
        dexterity = 0
        wisdom = 0
        intelligence = 0
        charisma = 0

        return strength, constitution, dexterity, wisdom, intelligence, charisma

    def tiefling():
        strength = 0
        constitution = 0
        dexterity = 0
        wisdom = 0
        intelligence = 1
        charisma = 2

        return strength, constitution, dexterity, wisdom, intelligence, charisma
