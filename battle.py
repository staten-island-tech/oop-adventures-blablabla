import stathandling as sh
import random as ran



class PlyrTurn:
    def attack(atk): ## player will attack 
        rand = ran.random(0.6, 1.5)
        statname -= atk * rand
    def ability(abil): ## player will use an ability 
        if abil == "slateskin":
            global playerDamageResist
            global playerStunnedTurns
            playerDamageResist += .2
            playerStunnedTurns = 1

class NpcTurn:
    def attack(atk, statname):
        rand = ran.random(0.6, 1.5)
        statname -= atk * rand
    def abil(abil):
        global playerEffects
        if abil == "poison_pwder":
            playerEffects.append({
                "name": "poison",
                "turns": 2
            })

isBattle = False
playerDamageResist = 0
playerDamageInflict = 0
playerStunnedTurns = 0
playerEffects = []

while isBattle == True:
    global curhp
    global npc_curhp
    global atk
    global npc_atk
    global passive
    for effect in playerEffects:
        if effect["name"] == "poison":
            if effect["turns"] < 1:
                playerEffects.remove(effect)
                print("The poison inflicted upon you has worn off.")
            else:
                curhp -= 6
                print("The poison inside your body drains your health.. ")
                effect["turns"] -= 1

        if effect["name"] == "weaken":
            if effect["turns"] < 1:
                playerEffects.remove(effect)
                print("The weakness you've been cursed with has withered away.")
            else:
                atk = atk - 3
                print("A powerful effect weakens your strength..")
                effect["turns"] -= 1
    
    print("<ATTACK> | <ABILITY>")
    option = input("What action would you like to do? >> ")
    if option.lower() == "attack":
        rand = ran.random(0.6, 2)
        npc_curhp -= atk * rand
        if rand > 1.5:
            print(f"Critical strike! You dealt {atk * rand} damage.")
        elif rand < .9:
            print(f"Your strike was weak! You dealt {atk * rand} damage.")
        else:
            print(f"On spot! You dealt {atk * rand} damage.")




            


            
            


