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
atk = 0
hp = 0




class Effects:
    def debuff(name: str, tier: int, time: int):
        if name == "weaken":
            dec(atk, (3*tier))
        elif name == "poison":
            dec(hp, (6*tier))
        while time > 1:
            time -= 1
        if time == 0:
            print(f"Effect {name} {tier} has ran out.")
    
    def buff(name: str, tier: int, time: int):
        if name == "strength":
            inc(atk, (3*tier))
        elif name == "poison":
            dec(hp, (6*tier))
        while time > 1:
            time -= 1
        if time == 0:
            print(f"Effect {name} {tier} has ran out.")


class PlyrTurn:
    def attack(atk, dmg: int):
        