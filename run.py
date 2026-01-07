class npc:
    
    def __init__(self, name, dialouge, atk, hp):
        self.__name=name
        self.__dialouge=dialouge
        self.__atk=atk
        self.__hp=hp
    
    def interaction(self):
        print(self.__dialouge)
        choice=input("would you like to end the conversation? Yes or No")
        if choice == "No":
            print("the Npc has wandered away")
        elif choice == "Yes":
            print(self.__dialouge)

    
    def status(self):
        print("**Npc's Stats**")
        print(f"Name:{self.__name}")
        print(f"Dialouge:{self.__dialouge}")
        print(f"Atk:{self.__atk}")
        print(f"Hp:{self.__hp}")
    
Npcbattle=[
    {"name":"Warlord","atk": 100, "hp": 100},
    {"name":"Pirate King", "atk": 99, "hp":200},
    {"name":"Zeus", "atk":77, "hp":88},
    {"name": "Moon God", "atk": 129, "hp":72}    
]

userchoice=int(input("choose a number from 0 to 3 to fight a random npc:"))
print("you will be fighting", Npcbattle[userchoice]["name"])

Npcfight=npc(Npcbattle[userchoice]["name"],"Let the fight begin", Npcbattle[userchoice]["atk"], Npcbattle[userchoice]["hp"])

while True:
    Npcfight.status()
    break

class boss(npc):
    




            

    


        
