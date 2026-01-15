## run this .py file to start the game
## DO NOT RUN ANY OTHER FILE!! tyy

import random as ran
import run as npc
import player as plyr
import math as m

class PlyrTurn:
    def attack(atk): ## player will attack 
        rand = ran.uniform(0.7, 1.5)
        dmg = (plyr.playerChar.atk * rand)
        battledNpc.hp -= m.ceil(dmg)
        return rand
    def ability(abil): ## player will use an ability 
        global playerStunnedTurns
        if abil == "Slateskin":
            playerStunnedTurns = 1
        if abil == "Sword":
            playerStunnedTurns = 1
            rand = ran.uniform(0.6, 1.5)
            dmg = (plyr.playerChar.atk * rand)* 1.10
            battledNpc.hp -= m.ceil(dmg)
            return dmg 
class NpcTurn:
    def attack(atk):
        rand = ran.uniform(0.5, 1.3)
        dmg = (battledNpc.atk * rand)
        plyr.playerChar.curhp -= m.floor(dmg)
        print(f"{battledNpc.name} attacked you and dealt {int(dmg)} damage!")

isBattle = False
while isBattle == False:
    plyr.chooseChar()
    battledNpc = npc.npcBattle()
    isBattle = True
playersTurn = True
playerStunnedTurns = 0
while isBattle == True:
    if battledNpc.hp <= 0:
        print(f"You have defeated {battledNpc.name}!")
        isBattle = False
        break
    if plyr.playerChar.curhp <= 0:
        print("You have been defeated.. Game Over!")
        isBattle = False
        break
    if playerStunnedTurns > 0:
        playerStunnedTurns -= 1
        print(" ")
        print("You are still recovering from your last ability use and cannot do anything this turn!")
        print(" ")
    elif playersTurn == True:
        if plyr.playerChar.abil == "Care":
            if plyr.playerChar.curhp + 5 > plyr.playerChar.maxhp:
                plyr.playerChar.curhp = plyr.playerChar.maxhp
            else:
                plyr.playerChar.curhp += 5
        print("<ATTACK> | <ABILITY> | <STATUS>")
        option = input("What action would you like to do? >> ")
        if option.lower() == "attack":
            rand = PlyrTurn.attack(plyr.playerChar.atk)
            if rand > 1.5:
                print(f"Critical strike! You dealt {int(plyr.playerChar.atk * rand)} damage.")
            elif rand < .9:
                print(f"Your strike was weak! You dealt {int(plyr.playerChar.atk * rand)} damage.")
            else:
                print(f"On spot! You dealt {int(plyr.playerChar.atk * rand)} damage.")
            print(" ")
            playersTurn = False
            continue
        elif option.lower() == "ability":
            print(f"You used your ability: {plyr.playerChar.abil}!")
            dmg = PlyrTurn.ability(plyr.playerChar.abil)
            if plyr.playerChar.abil == "Sword":
                print(f"Using your sharp sword, you managed to deal {int(dmg)} damage!")
                print("You spend the entirety of your next turn stashing your sword away though..")
                playersTurn = False
            elif plyr.playerChar.abil == "Slateskin":
                print(" ")
                print("You drank a Slateskin Potion, granting resistance to the next attack against you!")
                print("You are immobilized for the entirety of next turn as the effects wear off, though..")
                print("")
                playersTurn = False
            else:
                print("You dont have any usable non-passive abilities!")
        elif option.lower() == "status": ## does not end players turn
            plyr.playerChar.status()
            battledNpc.status()
            continue
    else: ## NPC TURN
        NpcTurn.attack(battledNpc.atk)
        playersTurn = True

            


        


            

        





            


            
            


