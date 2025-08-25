class Weapon:
    def __init__(self, weapon_type: str, damage: int):
        self._weapon_type = weapon_type #either sword, bow and arrow, staff
        self._damage = damage # damage done on each hit with a weapon

    
    @property
    def weapon_type(self):
        return self._weapon_type
    
    @weapon_type.setter
    def weapon_type(self, value: str):
        self._weapon_type = value

    
    @property
    def damage(self):
        return self._damage
    
    @damage.setter
    def damage(self, value: int):
        self._damage = value