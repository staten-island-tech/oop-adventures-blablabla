class npc:
    
    def __init__(self, name, dialouge, atk, hp,expgain):
        self.__name=name
        self.__dialouge=dialouge
        self.__atk=atk
        self.__hp=hp
        self.__expgain=expgain
    
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
        print(f"expgain:{self.__expgain}")

    def dead(self):
        return self.__hp <= 0
            #Here we would want to append exp into the players inventory and maybe append a boss drop of some sort






    
Npcbattle=[
    {"name":"Warlord","atk": 100, "hp": 100, "expgain": 45},
    {"name":"Pirate King", "atk": 99, "hp":200, "expgain":55},
    {"name":"Zeus", "atk":77, "hp":88, "expgain":66},
    {"name": "Moon God", "atk": 129, "hp":72, "expgain":77}
]

userchoice=int(input("choose a number from 0 to 3 to fight a random npc:"))
print("you will be fighting", Npcbattle[userchoice]["name"])


Npcfight=npc(Npcbattle[userchoice]["name"],"Let the fight begin", Npcbattle[userchoice]["atk"], Npcbattle[userchoice]["hp"], Npcbattle[userchoice]["expgain"])



    




            

    


        
