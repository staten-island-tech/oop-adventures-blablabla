import random as ran
import run as npc



class PlyrTurn:
    def attack(atk): ## player will attack 
        global npc_curhp
        rand = ran.random(0.6, 1.5)
        npc_curhp -= atk * rand
        return rand
    def ability(abil): ## player will use an ability 
        if abil == "slateskin":
            global playerDamageResist
            global playerStunnedTurns
            playerDamageResist += .2
            playerStunnedTurns = 1
        if abil == "sword":
            global npc_curhp
            global atk
            rand = ran.random(0.6, 1.5)
            npc_curhp -= (atk * rand)* 1.10
            return rand 


class NpcTurn:
    def attack(atk):
        global curhp
        rand = ran.random(0.9, 1.3)
        curhp -= atk * rand
        print(f"the NPC attacked you and dealt {atk * rand} damage!")
    def abil(abil):
        global playerEffects
        if abil == "poison_pwder":
            playerEffects.append({
                "name": "poison",
                "turns": 2
            })
            print("the NPC threw a poisonous powder at you! You are now poisoned.")

isBattle = False
playersTurn = True
playerDamageResist = 0
playerDamageInflict = 0
playerStunnedTurns = 0
while isBattle == True:
    if playersTurn == True:
        if playerStunnedTurns > 0:
            playersTurn == False
            continue
        if abil == "care":
            curhp += 5
        print("<ATTACK> | <ABILITY> | <STATUS>")
        option = input("What action would you like to do? >> ")
        if option.lower() == "attack":
            rand = PlyrTurn.attack(atk)
            if rand > 1.5:
                print(f"Critical strike! You dealt {atk * rand} damage.")
            elif rand < .9:
                print(f"Your strike was weak! You dealt {atk * rand} damage.")
            else:
                print(f"On spot! You dealt {atk * rand} damage.")
        elif option.lower() == "ability":
            doAbil = PlyrTurn.ability(abil)
            if abil == "sword":
                print(f"Using your sharp sword, you managed to deal {(atk*rand)*1.10} damage!")
                print("You spend the entirety of your next turn stashing your sword away though..")
            if abil == "slateskin":
                print("You drank a Slateskin Potion, granting resistance to the next attack against you!")
                print("You are immobilized for the entirety of next turn as the effects wear off, though..")
                
    else: ## NPC TURN
        if curhp < hp / 2:
            NpcTurn.attack(npc.npc_atk)
        elif npc.npc_curhp > npc.npc_maxhp / 2:
            rand = ran.randint(1,3)
            if rand != 3:
                NpcTurn.attack(npc.npc_atk)
            else:
                NpcTurn.attack("poison_pwder")

            


        


            

        





            


            
            


