import random as ran
import run as npc
import player as plyr



class PlyrTurn:
    def attack(atk): ## player will attack 
        rand = ran.uniform(0.6, 1.5)
        battledNpc.hp -= atk * rand
        return rand
    def ability(abil): ## player will use an ability 
        if abil == "Slateskin":
            global playerStunnedTurns
            playerStunnedTurns = 1
        if abil == "Sword":
            rand = ran.uniform(0.6, 1.5)
            battledNpc.hp -= (plyr.playerChar.atk * rand)* 1.10
            return rand 


class NpcTurn:
    def attack(atk):
        rand = ran.uniform(0.9, 1.3)
        plyr.playerChar.curhp -= atk * rand
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
    print(f"DEBUG: playerchar = {plyr.playerChar}")
    if playersTurn == True:
        if playerStunnedTurns > 0:
            playersTurn = False
            playerStunnedTurns -= 1
            continue
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
                print(f"Critical strike! You dealt {plyr.playerChar.atk * rand} damage.")
            elif rand < .9:
                print(f"Your strike was weak! You dealt {plyr.playerChar.atk * rand} damage.")
            else:
                print(f"On spot! You dealt {plyr.playerChar.atk * rand} damage.")
            playersTurn = False
            continue
        elif option.lower() == "ability":
            print(f"You used your ability: {plyr.playerChar.abil}!")
            doabil = PlyrTurn.ability(plyr.playerChar.abil)
            if plyr.playerChar.abil == "Sword":
                print(f"Using your sharp sword, you managed to deal {(plyr.playerChar.atk*doabil)*1.10} damage!")
                print("You spend the entirety of your next turn stashing your sword away though..")
                playersTurn = False
                continue
            elif plyr.playerChar.abil == "Slateskin":
                print("You drank a Slateskin Potion, granting resistance to the next attack against you!")
                print("You are immobilized for the entirety of next turn as the effects wear off, though..")
                playersTurn = False
                continue
            else:
                print("You dont have any usable non-passive abilities!")
        elif option.lower() == "status": ## does not end players turn
            print("**Player's Stats**")
            print(f"Name:{plyr.playerChar.name}")
            print(f"Atk:{plyr.playerChar.atk}")
            print(f"Hp:{plyr.playerChar.curhp}/{plyr.playerChar.maxhp}")
            print(f"Ability:{plyr.playerChar.abil}")
            battledNpc.status()
            continue
    else: ## NPC TURN
        NpcTurn.attack(battledNpc.atk)
        playersTurn = True
            


        


            

        





            


            
            


