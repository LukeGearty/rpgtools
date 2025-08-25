from archetype import *
from weapon import *

class Player:
    def __init__(self, archetype: Archetype, weapon: Weapon):
        """
        
        Takes in name, health, archetype, and weapon
        Archetype can be Warrior, Thief, or Mage
        Weapon can be Sword (warrior), Bow and Arrow (Thief), or Staff (Mage)

        """
        self._archetype = archetype
        self._weapon = weapon
        self._is_alive = True
    

    # character name
    @property
    def name(self):
        return self._archetype.name
    

    @name.setter
    def name(self, value: str):
        self._archetype.name = value

    

    #character class
    @property
    def vocation(self):
        return self._archetype.vocation
    
    @vocation.setter
    def vocation(self, value: str):
        self._archetype.vocation = value

    
    #weapon type
    @property
    def weapon(self):
        return self._weapon.weapon_type
    
    @weapon.setter
    def weapon(self, value: str):
        self._weapon.weapon_type = value


    #character health
    @property
    def health(self):
        return self._archetype.health
    

    @health.setter
    def health(self, value: int):
        self._archetype.health = value
    

    #character damage
    @property
    def damage(self):
        return self._weapon.damage
    

    #character is alive
    @property
    def is_alive(self):
        return self._is_alive
    
    @is_alive.setter
    def is_alive(self, value: bool):
        self._is_alive = value
    

    @damage.setter
    def damage(self, value: int):
        self._weapon.damage = value
    

    def take_damage(self, damage: int):
        new_health = self.health - damage
        if new_health <= 0:
            self.is_alive = False
            self.health = new_health
        else:
            self.health = new_health
