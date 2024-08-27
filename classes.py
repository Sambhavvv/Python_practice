class Footballer:

    def __init__(self,name,age,position,club):
        self.name=name
        self.age=age
        self.occupation=Footballer
        self.position=position
        self.club=club


    def show_Footballer(self):
        print("I am ",self.name,'and my age is',self.age,"\n",'I am a Footballer for',self.club,"and i play at",self.position)

Ronaldo = Footballer("Cristiano Ronaldo",39,"ST","AL NASSR") 
Messi= Footballer("Lionel Messi",38,'RW','INTER MIAMI')
Ronaldo.show_Footballer()
Messi.show_Footballer()
