class Archetype:
    def __init__(self, name: str, vocation: str, health: int):
        self._name = name
        self._vocation = vocation #either Warrior, Mage, Thief
        self._health = health
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value


    @property
    def vocation(self):
        return self._vocation
    
    @vocation.setter
    def vocation(self, value: str):
        self._vocation = value


    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value: int):
        self._health = value

