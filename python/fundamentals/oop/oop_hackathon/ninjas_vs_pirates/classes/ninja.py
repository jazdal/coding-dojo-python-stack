import random

class Ninja:
    technique = 0

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if self.can_fight(self.strength):
            pirate.health -= self.strength
            pirate.strength -= 3
            print('Ninja Attack!')
        else:
            print(f'{self.name} can\'t fight anymore!')
        return self
    
    def shuriken_strike(self, pirate):
        if self.can_fight(self.strength):
            pirate.health -= 5
            pirate.strength -= 1
            print('Shuriken Strike!')
        else:
            print(f'{self.name} can\'t fight anymore!')
        return self
    
    def sword_slash(self, pirate):
        if self.can_fight(self.strength):
            pirate.health -= 15
            pirate.strength -= 2
            print('Sword Slash!')
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

class Shinobi(Ninja):
    def __init__(self, name):
        super().__init__(name)
        self.strength = 20
        self.speed = 10
        self.health = 100
    
    def attack(self, pirate):
        print('Using special technique: Fire Breath!!!')
        super().attack(pirate)