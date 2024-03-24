class Person :
    def __init__(self,name,age,gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def Introduce(self) :
        print(f"Hi my name is {self.name}.I am {self.age} years old.I am {self.gender}.")
        
person1 = Person("samuel", 19, "Male")

person1.Introduce()

    
 

  
        
