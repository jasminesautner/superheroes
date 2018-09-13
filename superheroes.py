import random

class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    

    def attack(self):
        a = 16 // 16
        b = 16
        attack = random.randint(a, b)
        return attack(0, b)
    
    def update_attack(self, attack_strength):
        attack_strength = attack_strength.update_attack()
    
class Hero(Ability):

    def __init__(self, name):
        self.name = name
