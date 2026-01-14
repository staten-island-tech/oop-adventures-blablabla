import random as ran
import run as npc
import player as plyr



class PlyrTurn:
    def attack(atk): ## player will attack 
        rand = ran.random(0.6, 1.5)
        battledNpc._hp -= atk * rand
        return rand
    def ability(abil): ## player will use an ability 
        if abil == "slateskin":
            global playerStunnedTurns
            playerStunnedTurns = 1
        if abil == "sword":
            rand = ran.random(0.6, 1.5)
            battledNpc._hp -= (plyr.playerChar._atk * rand)* 1.10
            return rand 


class NpcTurn:
    def attack(atk):
        rand = ran.random(0.9, 1.3)
        plyr.playerChar._curhp -= atk * rand
        print(f"{battledNpc._name} attacked you and dealt {atk * rand} damage!")

isBattle = False
while isBattle == False:
    if plyr.playerChar == None:
        plyr.chooseChar()
    battledNpc = npc.npcBattle()
    isBattle = True
playersTurn = True
playerStunnedTurns = 0
while isBattle == True:
    if plyr.playerChar._curhp <= 0:
        print("You have been defeated...")
        isBattle = False
        break
    elif battledNpc._hp <= 0:
        print(f"You have defeated the {battledNpc._name}!")
        isBattle = False
        break
    if playersTurn == True:
        if playerStunnedTurns > 0:
            playersTurn = False
            playerStunnedTurns -= 1
            continue
        if plyr.playerChar._abil == "care":
            plyr.playerChar._curhp += 5
        print("<ATTACK> | <ABILITY> | <STATUS>")
        option = input("What action would you like to do? >> ")
        if option.lower() == "attack":
            rand = PlyrTurn.attack(plyr.playerChar._atk)
            if rand > 1.5:
                print(f"Critical strike! You dealt {plyr.playerChar._atk * rand} damage.")
            elif rand < .9:
                print(f"Your strike was weak! You dealt {plyr.playerChar._atk * rand} damage.")
            else:
                print(f"On spot! You dealt {plyr.playerChar._atk * rand} damage.")
        elif option.lower() == "ability":
            rand = PlyrTurn.ability(plyr.playerChar._abil)
            if plyr.playerChar._abil == "sword":
                print(f"Using your sharp sword, you managed to deal {(plyr.playerChar._atk*rand)*1.10} damage!")
                print("You spend the entirety of your next turn stashing your sword away though..")
            if plyr.playerChar._abil == "slateskin":
                print("You drank a Slateskin Potion, granting resistance to the next attack against you!")
                print("You are immobilized for the entirety of next turn as the effects wear off, though..")
        elif option.lower() == "status": ## does not end players turn
            print("**Player's Stats**")
            print(f"Name:{plyr.playerChar._name}")
            print(f"Atk:{plyr.playerChar._atk}")
            print(f"Hp:{plyr.playerChar._curhp}/{plyr.playerChar._maxhp}")
            print(f"Ability:{plyr.playerChar._abil}")
            battledNpc.status()
            continue
    else: ## NPC TURN
        NpcTurn.attack(battledNpc._atk)
        playersTurn = True
            


        


            

        





            


            
            


