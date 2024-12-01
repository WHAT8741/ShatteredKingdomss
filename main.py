import random
import time

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

Player_health = 100
Elf_health = 70
weapon = input("Choose your weapon (Sword/Bow): ")
melee = 0
ranged = 0
if weapon == "Sword":
  melee += 10
if weapon == "Bow":
  ranged += 10


print("You are walking through the woods and you come across an Elf.")
time.sleep(3)
print("He stands guard at the entrance to a dark and forgotten temple.  He warns you to turn back.")
time.sleep(3)
print("But you know this Elf is a minion of your father, who killed your mother. He is a very strong Elf.")
time.sleep(3)
print("You must fight him.")


def attack():
  global Player_health
  global Elf_health
  global weapon
  round_number = 1

  while Player_health > 0 and Elf_health > 0:
    print(f"Round {round_number}")
    print(f"Your Health: {Player_health}")
    print(f"Elf's Health: {Elf_health}")

    # Player's Attack
    attack_roll = random.randint(1, 20)
    if attack_roll == 1 or attack_roll == 2 or attack_roll == 3 or attack_roll == 4:
      print("You missed!")
    else:
        damage = min((attack_roll - 4) * 2, 20)  # Cap damage at 20
        defense = random.randint(1, 20)
        damage_dealt = max(0, damage - defense)  # Prevent negative damage
        print(f"You did {damage_dealt} damage, because the Elf blocked {defense} damage.")
        Elf_health -= damage_dealt

    if Elf_health <= 0:
      print("You killed the Elf!")
      break

    # Elf's Attack
    elf_attack_roll = random.randint(1, 20)
    if elf_attack_roll == 1 or elf_attack_roll == 2 or elf_attack_roll == 3 or elf_attack_roll == 4:
      print("The Elf missed!")
    else:
      damage = min((elf_attack_roll - 4) * 2, 20)
      defense = random.randint(1, 20)
      damage_dealt = max(0, damage - defense)
      print(f"The Elf did {damage_dealt} damage to you!")
      Player_health -= damage_dealt

    if Player_health <= 0:
      print("You died!")
      break

    round_number += 1
    time.sleep(3)

attack()

answer = input("You have killed the Elf.  What do you do next? (1) Enter the temple, (2) Search the Elf's body, (3) Leave the woods. ")

if answer == "1":
  print("You enter the temple, and you see a large room with a large chest in the center.")
  time.sleep(3)
  choice = input("Do you open the chest? (yes/no) ")
  if choice == "yes":
    print("You open the chest, but smoke fills the room, and you fall to the ground, that's what you get for being a greedy B@stard.")
    time.sleep(10)
    print("You wake up, seeing a large Elf standing over you, and he says, 'You greedy B@stard', and shows you the mines, he sneers'You will work for me in the crytal mines forever and never leave.'")
    choice1 = input("Do you. A) Accept his offer, B) hit him unarmed. ")
    if choice1 == "A": 
      print("You accept his offer, and you work for him in the mines, and you live horribly ever after.")
      time.sleep(10)
      print("You have been here for 20 years, you have seen many of the minors/miners want to start a reballion, and you have been the leader of the rebellion for 15 years. You have the proper resources and guys to help you, but you have no idea what to do. You have been in the mines for 20 years, and still fear the wicked elf, but you know that your father is still alive, and you know that he will be back soon. You have been waiting over 20 years for this moment, and you know that you have to do something. You know that you have to kill your father, and you know that you have to kill the elf, and you have gained spells and knowledge of the mines from the other miners, this is the reballion you have been waiting for. You grab your men and weapons. The Elf sees you, he takes his shirt off, reveals his face, and says, 'You greedy B@stard', and shows his abs,there is energy around him, he takes his greatsword of crytal out, and you see the energy, and you know that you have to kill him. You grab your men and weapons, and the Elf sneers bring it on. ")
      choice2 = input(" What do you do? A) attack him with your weapon")
      Elf_health2 = 200
      if choice2 == "A":
        attack_roll = random.randint(1, 20)
        if attack_roll == 1 or attack_roll == 2 or attack_roll == 3 or attack_roll == 4:
          print("You missed!")
        else:
            damage = min((attack_roll - 4) * 2, 20)
            defense = random.randint(1, 30)
            damage_dealt = max(0, damage - defense)  # Prevent negative damage
            print(f"You did {damage_dealt} damage, because the Elf blocked {defense} damage.")
            Elf_health -= damage_dealt
      print("It is now your men's turn to attack, but the elf is too strong, and he is too fast, and you have no time to think, and right before you almost all of your army is sliced, the dark energy feeling the air with scent, only derek is alive.Roll a Dexterity check to dodge the greatsword.")
      dexterity_check = random.randint(1, 20) + Dexterity/10 + 2 
      if dexterity_check <= 7:
        print("You died")
      elif dexterity_check >= 7:
        print("You dodge the greatsword and stab the elf, make a strengh check to see if you can harm him.")
        strength_check = random.randint(1, 20) + Strength/10 + 2
        if strength_check >= 10:
          attack_roll = random.randint(1, 20)
          if attack_roll == 1 or attack_roll == 2 or attack_roll == 3 or attack_roll == 4:
            print("You missed!")
          else:
              damage = min((attack_roll - 4) * 2, 20)
              defense = random.randint(1, 30)
              damage_dealt = max(0, damage - defense)  # Prevent negative damage
              print(f"You did {damage_dealt} damage, because the Elf blocked {defense} damage.")
              Elf_health -= damage_dealt
          print("You successfully harm the elf! You grab your men and weapons, and the Elf sneers bring it on. But he throws a purple rock at you, and you feel a sharp pain in your chest, and you fall to the ground, but as your vision blacks out, you see a hooded woman stab her dagger through the skull of the Elf, and then your vison blacks out.")
          time.sleep(10)
    elif choice1 == "B":
      print("You hit him unarmed, and he kills you.")
      time.sleep(100000000000000000000000000000000000)
      
print("You wake up in the woods, you are lying besides a fireplace, and you see the woman, she introduces her self as
