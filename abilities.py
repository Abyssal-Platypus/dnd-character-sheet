#!/usr/bin/env python3
# coding=utf-8

"""
The 'heavy lifting' math, information from the char_sheet.py file gets passed 
through these series of functions and returns the modifier. 

Brandon Cowan
"""

class Abilities():

    def strength(s_total):
        base = s_total - 10
        s_mod = base // 2
        return s_mod

    def constitution(c_total):
        base = c_total - 10
        c_mod = base // 2
        return c_mod

    def dexterity(d_total):
        base = d_total - 10
        d_mod = base // 2
        return d_mod

    def wisdom(w_total):
        base = w_total - 10
        w_mod = base // 2
        return w_mod
        
    def intelligence(i_total):
        base = i_total
        i_mod = base // 2
        return i_mod
        
    def charisma(ch_total):
        base = ch_total
        ch_mod = base // 2
        return ch_mod
