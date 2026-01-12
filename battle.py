import random as ran



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

isBattle = False
playersTurn = True
playerStunnedTurns = 0

while isBattle == True:
    if curhp < 1:
        print("You died! :(")
        isBattle = False
    if playerStunnedTurns > 0:
        playersTurn == False
        print("Your turn was skipped because you were stunned!")
        playerStunnedTurns -= 1
    if playersTurn == True:
        if playerStunnedTurns > 0:
            playersTurn == False
            playerStunnedTurns -= 1
        if abil == "care":
            curhp += 5 + level

        
        print("<ATTACK> | <ABILITY>")
        option = input("What action would you like to do? >> ")
        if option.lower() == "attack":
            rand = PlyrTurn.attack(atk)
            if rand > 1.5:
                print(f"Critical strike! You dealt {atk * rand} damage.")
            elif rand < .9:
                print(f"Your strike was weak! You dealt {atk * rand} damage.")
            else:
                print(f"On spot! You dealt {atk * rand} damage.")
        if option.lower() == "ability":
            doAbil = PlyrTurn.ability(abil)
            if abil == "sword":
                print(f"Using your sharp sword, you managed to deal {(atk*rand)*1.10} damage!")
                print("You spend the entirety of your next turn stashing your sword away though..")
            if abil == "slateskin":
                print("You drank a Slateskin Potion, granting resistance to the next attack against you!")
                print("You are immobilized for the entirety of next turn as the effects wear off, though..")
    else: ## NPC TURN
        if npc_curhp < 1:
            print("You killed the NPC!")
            isBattle = False
            break
        rand = ran.randint(1,3)
        if rand != 3:
            NpcTurn.attack(npc_atk)
            

        


            

        





            


            
            


