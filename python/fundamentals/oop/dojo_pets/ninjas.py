import pets

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        print()
        print(f'{self.first_name} played with {self.pet.name}.')
        self.pet.play()
        return self
    
    def feed(self):
        print()
        print(f'{self.first_name} gave {self.pet.name} {self.treats} and {self.pet_food}.')
        self.pet.eat()
        return self
    
    def bathe(self):
        print()
        print(f'{self.first_name} gave {self.pet.name} a bath!')
        self.pet.noise()
        return self

naruto = Ninja("Naruto", "Uzumaki", "cookies", "bone", pets.Pet("Milo", "Dog", "Destroy", "Bark!"))
naruto.walk().feed().bathe()

harry = Ninja("Harry", "Potter", "mice", "bird seed", pets.Aerial("Hedwig", "Owl", "Divebomb", "Coo!", 0.5))
harry.bathe().pet.fly()