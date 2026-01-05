import stathandling as sh
import player

class Effects:
    def debuff(name: str, tier: int, time: int):
        if name == "weaken":
            sh.dec(atk, (3*tier))
        elif name == "poison":
            sh.dec(hp, (6*tier))
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
    def attack(atk): ## player will attack and end their turn
        
    def ability(abil): ## player will use an ability and end their turn

    def item(item): ## player will use an item and end their turn