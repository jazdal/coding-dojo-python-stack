class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 5
        self.energy = 5
    
    def sleep(self):
        self.energy += 25
        print(f'{self.name} gained +25 energy. Current energy is: {self.energy}.')
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'{self.name} gained +5 energy and +10 health. Current energy is: {self.energy}. Current health is: {self.health}.')
        return self
    
    def play(self):
        self.health += 5
        print(f'{self.name} gained +5 health. Current health is: {self.health}.')
        return self
    
    def noise(self):
        print(f'{self.name}: {(self.sound + " ") * 3}')
        return self

class Aerial(Pet):
    def __init__(self, name, type, tricks, sound, wingspan):
        super().__init__(name, type, tricks, sound)
        self.wingspan = wingspan
    
    def fly(self):
        self.health += 10
        print()
        print(f'{self.name} fully-stretched its {self.wingspan}-meter wings and flew up high into the sky!')
        print(f'{self.name} gained +10 health. Current health is: {self.health}')
        return self