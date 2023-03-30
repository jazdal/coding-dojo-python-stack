import random

class Pirate:
    technique = 0

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if self.can_fight(self.strength):
            ninja.health -= self.strength
            ninja.strength -= 3
            print('Pirate Attack!')
        else:
            print(f'{self.name} can\'t fight anymore!')
        return self
    
    def hook_hand(self, ninja):
        if self.can_fight(self.strength):
            ninja.health -= 5
            ninja.strength -= 1
            print('Hook Hand Attack!')
        else:
            print(f'{self.name} can\'t fight anymore!')
        return self
    
    def cannonball(self, ninja):
        if self.can_fight(self.strength):
            ninja.health -= 15
            ninja.strength -= 2
            print('Cannon Ball Fire!')
        else:
            print(f'{self.name} can\'t fight anymore!')
        return self
    
    @classmethod
    def determine_technique(cls):
        cls.technique = random.randint(1,3)
        return cls.technique
    
    @staticmethod
    def can_fight(strength):
        if strength > 0:
            return True
        else:
            return False

class Corsair(Pirate):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 20
        self.speed = 5
        self.health = 100
    
    def attack(self, ninja):
        print(f'Using special technique: Devil Fruit Attack!!!')
        super().attack(ninja)