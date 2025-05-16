class Human:
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def checkgender(self):
        if self.gender == 'Male':
            print(f"His name is {self.name}. He is {self.age} years old")
        else:
            print(f"Her name is {self.name}. She is {self.age} years old")
        
    def compare_age(self,other):
        if self.age > other.age:
            print(f"{self.name} is older than {other.name}")
        elif self.age == other.age:
            print(f"{self.name} and {other.name} are of same age")
        else:
            print(f"{self.name} is younger than {other.name}")
        

human1 = Human("AP",26,'Male')
human1.checkgender()

human2 = Human("ANP",32,'Female')
human2.checkgender()    

human2.compare_age(human1)



