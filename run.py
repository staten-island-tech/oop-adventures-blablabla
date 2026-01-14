## This is the file containing pretty much all npc-related code.
## DO NOT RUN THIS FILE DIRECTLY. run battle.py to start the game.


class npc:
    
    def __init__(self, name, dialouge, atk, hp):
        self.name=name
        self.dialouge=dialouge
        self.atk=atk
        self.hp=hp

    def interaction(self):
        choice=input("would you like to hear the npc's backstory? Yes or No:")
        if choice.lower() == "no":
            print("Very well")
        elif choice.lower() == "yes":
            print("I was borned at a very young age, I could only cry, I couldn't walk, and I was borned blinded ")


    def status(self):
        print("**Npc's Stats**")
        print(f"Name:{self.name}")
        print(f"Dialouge:{self.dialouge}")
        print(f"Atk:{self.atk}")
        print(f"Hp:{self.hp}")


npcs =[
    {"name":"Fiend","atk": 7, "hp": 40},
    {"name":"Pirate", "atk": 9, "hp":60},
    {"name":"Ghoul", "atk":14, "hp":70},
    {"name": "Beast", "atk": 12, "hp":120}
]


def npcBattle():
    npcChosen = False
    while npcChosen == False:
        print("Choose a number from 1 to 4 to fight an NPC.")
        npcsel = input(">>> ") 
        if not npcsel.isdigit():
            print("You didnt choose a valid number!")
        elif int(npcsel) < 1 or int(npcsel) > 4:
            print("You didnt choose a valid number!")
        else:
            npcChosen = True
            return npc(npcs[int(npcsel)-1]["name"], "An enemy approaches!", npcs[int(npcsel)-1]["atk"], npcs[int(npcsel)-1]["hp"])
              




            

    


        
