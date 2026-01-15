## This is the file containing pretty much all player-related code.
## DO NOT RUN THIS FILE DIRECTLY. run battle.py to start the game.



class player:
    def __init__(self, name: str, atk: int, maxhp: int, curhp: int, abil):
        self.name = name
        self.atk = atk
        self.maxhp = maxhp
        self.curhp = curhp
        self.abil = abil
    def status(self):
            print("**Player's Stats**")
            print(f"Name:{self.name}")
            print(f"Atk:{self.atk}")
            print(f"Hp:{self.curhp}/{self.maxhp}")
            print(f"Ability:{self.abil}")

chars = [
    {
        "name": "shedletsky",
        "atk": 10,
        "hp": 90,
        "abil": "Sword",
        "abildesc": "Shedletsky always wields a very sharp sword on him, allowing him to deal 10 percent extra damage. Unable to move the following turn."
    },
    {
        "name": "noob",
        "atk": 8,
        "hp": 100,
        "abil": "Slateskin",
        "abildesc": "Noob is able to consume a Slateskin potion, resisting 40 percent of damage inflicted. Unable to moe the following turn."
    },
    {
        "name": "carepad",
        "atk": 5,
        "hp": 65,
        "abil": "Care",
        "abildesc": "Carepad naturally restores 5 HP every turn."
    }
]

## reminder: use playerChar.__<var> to access stats
playerChar = None
def chooseChar():
    global playerChar
    for char in chars:
        print("===========================")
        print(char["name"])
        print(f"{char["atk"]} ATK")
        print(f"{char["hp"]} MAX HP")
        print(f"{char["abil"]} Ability:")
        print(char["abildesc"])
    while playerChar == None:
        print("Please type in the name of the character you wish to play as.")
        selection = input(">>>")
        for char in chars:
            if char["name"] == selection.lower():
                playerChar = player(char["name"], char["atk"], char["hp"], char["hp"], char["abil"])
                print(f"You chose: {char["name"]}")
                Found = True
                break
            else:
                print("X")
                Found = False
        if Found == False:
            print("You did not select a valid character. Please retry!")
            continue

        
        