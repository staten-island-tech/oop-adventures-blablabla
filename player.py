class player:
    def __init__(self, name: str, atk: int, maxhp: int):
        self.name = name
        self.atk = atk
        self.maxhp = maxhp
        self.curhp = maxhp
    def dec(stat, amt: int):
        if stat == atk:
            atk -= amt
        elif stat == hp:
            hp -= amt
    def inc(stat, amt: int):
        if stat == atk:
            atk += amt
        elif stat == hp:
            hp += amt

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


playerChar = None
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
            playerChar = player(char["name"], char["atk"], char["hp"])
            atk = char["atk"]
            maxhp = char["hp"]
            curhp = maxhp
            print(f"You chose: {char["name"]}")
            Found = True
            break
        else:
            print("X")
            Found = False
    if Found == False:
        print("You did not select a valid character. Please retry!")
        continue

        
        