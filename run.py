class npc:
    
    def __init_(self, name, dialouge, atk, hp):
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

    
    def 
            

    


        

        


