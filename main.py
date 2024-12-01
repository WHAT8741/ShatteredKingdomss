import random
import time
import sys

Strength = random.randint(1, 20)
print(f"Your strength is {Strength}")
Intelligence = random.randint(1, 20)
print(f"Your intelligence is {Intelligence}")
Dexterity = random.randint(1, 20)
print(f"Your Dex is {Dexterity}")
Constitution = random.randint(1, 20)
print(f"Your constitution is {Constitution}")
Wisdom = random.randint(1, 20)
print(f"Your wisdom is {Wisdom}")
Charisma = random.randint(1, 20)
print(f"Your charisma is {Charisma}")

class Player:
  def __init__(self, name, role, health, str, dex, con, intell, wis, cha, gp):
    self.name = name
    self.role = role
    self.health = health
    self.str = str
    self.dex = dex
    self.con = con
    self.intell = intell
    self.wis = wis
    self.cha = cha
    self.gp = gp
PlayerIG = Player("Player", "class", 1, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, 0)
