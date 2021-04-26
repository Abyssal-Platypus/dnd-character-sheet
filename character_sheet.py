#!/usr/bin/env python3
# coding+=utf-8

"""
This is the original Kivy program that I was working with, I got really
far into it but when I started to build the Labels for the modifier 
outputs I kept getting the repr location or a different type of output.
Kivy will take a lot more effort and practice to get working for this
type of program. I would really like to finish building with this
module because of how it can work with Android OS. 

There is a lot going on here but the char_sheet.py file is modeled very
closely after this one. Even down to the same layout.

Brandon Cowan
"""

import abilities
import races
import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AbilityDisplay(GridLayout):
    def __init__(self, **kwargs):
        super(AbilityDisplay, self).__init__(**kwargs)
        self.cols = 3

        if os.path.isfile("character1.txt"):
            with open("character1.txt", "r") as f:
                d = f.read().split(",")
                character_name = d[0]
                char_str = d[1]
                char_con = d[2]
                char_dex = d[3]
                char_wis = d[4]
                char_int = d[5]
                char_cha = d[6]
        else:
            character_name = ''
            char_str = ''
            char_con = ''
            char_dex = ''
            char_wis = ''
            char_int = ''
            char_cha = ''

        self.add_widget(Label(text = 'Name'))
        self.name = TextInput(text = character_name, multiline = False)
        self.add_widget(self.name)
        self.add_widget(Label())
        self.add_widget(Label(text = 'Strength'))
        self.strength = TextInput(text = char_str, multiline = False) 
        self.add_widget(self.strength)
        self.add_widget(Label(text = str(Player.p_strength)))
        self.add_widget(Label(text = 'Constitution'))
        self.constitution = TextInput(text = char_con, multiline = False)
        self.add_widget(self.constitution)
        self.add_widget(Label(text = str(Player.p_constitution)))
        self.add_widget(Label(text = 'Dexterity'))
        self.dexterity = TextInput(text = char_dex, multiline = False)
        self.add_widget(self.dexterity)
        self.add_widget(Label(text = str(Player.p_dexterity)))
        self.add_widget(Label(text = 'Wisdom'))
        self.wisdom = TextInput(text = char_wis, multiline = False)
        self.add_widget(self.wisdom)
        self.add_widget(Label(text = str(Player.p_wisdom)))
        self.add_widget(Label(text = 'Intelligence'))
        self.intelligence = TextInput(text = char_int, multiline = False)
        self.add_widget(self.intelligence)
        self.add_widget(Label(text = str(Player.p_intelligence)))
        self.add_widget(Label(text = 'Charisma'))
        self.charisma = TextInput(text = char_cha, multiline = False)
        self.add_widget(self.charisma)
        self.add_widget(Label(text = str(Player.p_charisma)))

        self.save = Button(text = 'Save')
        self.save.bind(on_press = self.save_state)
        self.add_widget(Label())
        self.add_widget(self.save)

    def save_state(self, instance):
        character_name = self.name.text
        char_str = self.strength.text
        char_con = self.constitution.text
        char_dex = self.dexterity.text
        char_wis = self.wisdom.text
        char_int = self.intelligence.text
        char_cha = self.charisma.text

        print(f"Saving {character_name}.")

        with open("character1.txt", "w") as f:
            f.write(
                f"{character_name},{char_str},{char_con},{char_dex},{char_wis},{char_int},{char_cha}"
                )

class TheApp(App):
    def build(self):
        return AbilityDisplay()

class Player():

    def p_name(self):
        return p_name(App.get_running_app().root.name.text)
    
    def p_strength(self):
        strength_input = int(App.get_running_app().root.strength.text)
        racial_bonus = 0
        s_total = strength_input + racial_bonus
        s_modifier = abilities.strength(s_total)
        return s_modifier()

    def p_constitution(self):
        con_input = int(App.get_running_app().root.constitution.text)
        racial_bonus = 0
        c_total = con_input + racial_bonus
        c_modifier = abilities.constituation(c_total)
        return c_modifier()

    def p_dexterity(self):
        dex_input = int(App.get_running_app().root.dexterity.text)
        racial_bonus = 0
        d_total = dex_input + racial_bonus
        d_modifier = abilities.dexterity(d_total)
        return d_modifier()

    def p_wisdom(self):
        wis_input = int(App.get_running_app().root.wisdom.text)
        racial_bonus = 0
        w_total = wis_input + racial_bonus
        w_modifier = abilities.wisdom(w_total)
        return w_modifier()

    def p_intelligence(self):
        int_input = int(App.get_running_app().root.wisdom.text)
        racial_bonus = 0
        i_total = int_input + racial_bonus
        i_modifier = abilities.intelligence(i_total)
        return i_modifier()

    def p_charisma(self):
        cha_input = int(App.get_running_app().root.charisma.text)
        racial_bonus = 0
        ch_total = cha_input + racial_bonus
        ch_modifier = abilities.charisma(ch_total)
        return ch_modifier()
    
def main():
    char_name = AbilityDisplay.name

if __name__ == '__main__':
    TheApp().run()