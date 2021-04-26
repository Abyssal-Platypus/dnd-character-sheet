#! /usr/bin/env python3
# coding=utf-8

"""
This program is for a D&D character sheet. The goals of the program are
to allow a player to input their character informatioin such as name,
race, and ability stats, and have the program update the modifiers in real
time. Then place the modifiers in the proper locations for skills and any
other area where the ability modifiers are needed. The player will also be
able to save their character sheet for future use. The sheet will save as a 
text file seperated by commas for easy placement into the proper variables. 

As the program sits now, the math for the modifiers is there as well as the 
start of the sheet, the most important part being the abilities. The math 
for the ability modifiers is held in the abilities.py file, there is also 
a file holding the race ability modifiers, races.py. Honestly this turned
out to be a much harder program to build than I originially imagined. I 
first tried using Kivy but was unable to get the modifiers to return to 
the proper label box, I was only receiving the repr location. Sadly I wish 
I could have gotten further into the program, I feel like I'm really close 
to getting everything to work but something is eluding me here. I will
include the Kivy code that I was working on as well. Due to switching from
Kivy to TKinter well after I started building the code I was not able to 
get as much done as I had hoped.

Also with this code here, it will save a file for the character but it is
not saving the actual inputs. The way that its supposed to work is, save
the info into a text file and if there is a file that exists that matches
what the file would be named it would pull the text info and place it into
the input fields. 

Brandon Cowan
"""

from tkinter import *
import abilities
import races
import os

class AbilitySheet(Frame):
    """
    The master function that will create and call other functions, one function
    to rule them all. Class?
    """

    def __init__(self, master = None):
        Frame.__init__(self, master)
        """
        This is the window constructor, takes the fields as defined by the 
        various functions below and places them in the window.
        """
        self.master = master
        self.ability_plate()
        self.ability_input()
        
        menu = Menu(self.master)
        self.master.config(menu = menu)
        file = Menu(menu)
        file.add_command(label = 'Save', command = self.save_state)
        menu.add_cascade(label = 'File', menu = file)
        """This will create the top menu, simply for saving the character. """

        if os.path.isfile("character1.txt"):
            with open("character1.txt", "r") as f:
                d = f.read().split(",")
                self.name_input = Entry(text = d[0])
                self.str_input = Entry(text = d[1])
                self.con_input = Entry(text = d[2])
                self.dex_input = Entry(text = d[3])
                self.wis_input = Entry(text = d[4])
                self.int_input = Entry(text = d[5])
                self.cha_input = Entry(text = d[6])
        else:
            name_input = ''
            str_input = ''
            con_input = ''
            dex_input = ''
            wis_input = ''
            int_input = ''
            cha_input = ''

        """File I/O for finding a pre-existing character, and relaying inputs. """

    def ability_plate(self):
        """ 
        This function will place the labels for each section of the character
        sheet, name, strength, constitution and so on. This also uses the location
        based on XY coordinates.
        """
        self.master.title('GUI')
        self.pack(fill = BOTH, expand = 1)
        name_plate = Label(text = 'Name')
        name_plate.pack()
        name_plate.place(x = 0, y = 0)
        str_plate = Label(text = 'Strength')
        str_plate.pack()
        str_plate.place(x = 0, y = 25)
        con_plate = Label(text = 'Constitution')
        con_plate.pack()
        con_plate.place(x = 0, y = 50)
        dex_plate = Label(text = 'Dexterity')
        dex_plate.pack()
        dex_plate.place(x = 0, y = 75)
        wis_plate = Label(text = 'Wisdom')
        wis_plate.pack()
        wis_plate.place(x = 0, y = 100)
        int_plate = Label(text = 'Intelligence')
        int_plate.pack()
        int_plate.place(x = 0, y = 125)
        cha_plate = Label(text = 'Charisma')
        cha_plate.pack()
        cha_plate.place(x = 0, y = 150)


    def ability_input(self):
        """
        This function, a list of widgets, takes builds the entry fields for user
        input, starts by creating an entry box, packs it into the window. Then
        the last part of each section declares its location 
        """
        self.name_input = Entry(text = '')
        self.name_input.pack()
        self.name_input.place(x = 100, y = 0)

        self.str_input = Entry(text = '')
        self.str_input.pack()
        self.str_input.place(x = 100, y = 25)

        self.con_input = Entry(text = '')
        self.con_input.pack()
        self.con_input.place(x = 100, y = 50)

        self.dex_input = Entry(text = '')
        self.dex_input.pack()
        self.dex_input.place(x = 100, y = 75)

        self.wis_input = Entry(text = '')
        self.wis_input.pack()
        self.wis_input.place(x = 100, y = 100)

        self.int_input = Entry(text = '')
        self.int_input.pack()
        self.int_input.place(x = 100, y = 125)

        self.cha_input = Entry(text = '')
        self.cha_input.pack()
        self.cha_input.place(x = 100, y = 150)
    

    def save_state(self):
        """
        When the user clicks to save the character in the drop menu, this function
        will get the inputs from the entry fields and save them under a variable. 
        Then the function will write a text file with each variable in a string
        seperated by commas for future use.
        """
        name_input = self.name_input.get
        str_input = self.str_input.get
        con_input = self.con_input.get
        dex_input = self.dex_input.get
        wis_input = self.wis_input.get
        int_input = self.int_input.get
        cha_input = self.cha_input.get

        print(f"Saving {name_input}.")

        with open("character1.txt", "w") as f:
            f.write(
                f"{name_input},{str_input},{con_input},{dex_input},{wis_input},{int_input},{cha_input}"
                )

    def p_strength(self):
        """
        Function built to take the user input, find modifier and return to the output
        box. Each function that follows, p_constitution, p_dexterity and so on will do
        the same thing as this first function.
        """
        self.strength_input = self.str_input.get
        self.racial_bonus = 0
        self.s_total = strength_input + racial_bonus
        self.s_modifier = abilities.strength(s_total)
        return self.s_modifier

    def p_constitution(self):
        constitution_input = int(self.con_input.get)
        racial_bonus = 0
        c_total = self.con_input + racial_bonus
        c_modifier = abilities.constituation(c_total)
        return c_modifier()

    def p_dexterity(self):
        dextertity_input = int(self.dex_input.get)
        racial_bonus = 0
        d_total = self.dex_input + racial_bonus
        d_modifier = abilities.dexterity(d_total)
        return d_modifier()

    def p_wisdom(self):
        wisdom_input = int(self.wis_input.get)
        racial_bonus = 0
        w_total = self.wis_input + racial_bonus
        w_modifier = abilities.wisdom(w_total)
        return w_modifier()

    def p_intelligence(self):
        inttelligence_input = int(self.int_input.get)
        racial_bonus = 0
        i_total = self.int_input + racial_bonus
        i_modifier = abilities.intelligence(i_total)
        return i_modifier()

    def p_charisma(self):
        charisma_input = int(self.cha_input.get)
        racial_bonus = 0
        ch_total = self.cha_input + racial_bonus
        ch_modifier = abilities.charisma(ch_total)
        return ch_modifier()

root = Tk()
root.geometry('500x500')
"""Determine the size of the GUI window. """

app = AbilitySheet(root)

root.mainloop()