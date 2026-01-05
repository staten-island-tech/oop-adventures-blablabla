class boss:
    def __init_(self, name, attackdamage, specialbossdrop, health):
        self.name=name
        self.__attackdamgage=attackdamage
        self.__specialbossdrop=specialbossdrop
        self.__health=health

    def is_defeated(self):
        return self.__health < 0
        #now we want to append whatever the bosses drop into the hero's inventory