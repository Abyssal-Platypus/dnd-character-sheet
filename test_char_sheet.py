#! /usr/bin/env python3
# coding=utf-8

"""
I honestly do not know how I'm supposed to test a live application such
as a file made through Tkinter while its running. So I tested the math
from the abilities.py file to make sure that the proper modifiers would
be returned. 

Brandon Cowan
"""
import pytest

from abilities import Abilities

def test_strength():
    assert Abilities.strength(18) == 4

def test_con():
    assert Abilities.constitution(10) == 0

def test_dex():
    assert Abilities.dexterity(15) == 2

def test_wis():
    assert Abilities.wisdom(8) == -1

def test_int():
    assert Abilities.intelligence(0) == -5

def test_cha():
    assert Abilities.charisma(20) == 5

