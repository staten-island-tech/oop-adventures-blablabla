class npc:
    
    def __init__(self, name, dialouge, atk, hp):
        self.__name=name
        self.__dialouge=dialouge
        self.__atk=atk
        self.__hp=hp
    
    def interaction(self):
        choice=input("would you like to hear the npc's backstory? Yes or No:")
        if choice.lower() == "no":
            print("Very well")
        elif choice.lower() == "yes":
            print("I was borned at a very young age, I could only cry, I couldn't walk, and I was borned blinded ")


    def status(self):
        print("**Npc's Stats**")
        print(f"Name:{self.__name}")
        print(f"Dialouge:{self.__dialouge}")
        print(f"Atk:{self.__atk}")
        print(f"Hp:{self.__hp}")


npcs =[
    {"name":"Warlord","atk": 100, "hp": 100, "expgain": 45},
    {"name":"Pirate King", "atk": 99, "hp":200, "expgain":55},
    {"name":"Zeus", "atk":77, "hp":88, "expgain":66},
    {"name": "Moon God", "atk": 129, "hp":72, "expgain":77}
]

def npcBattle():
    npcChosen = False
    while npcChosen == False:
        print("Choose a number from 1 to 4 to fight an NPC.")
        npcsel = input(">>> ") 
        if npcsel < 1:
            print("You didnt choose a valid number!")
        elif npcsel > 4:
              




            

    


        
