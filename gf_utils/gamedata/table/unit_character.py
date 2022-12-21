
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class UnitCharacterInstance:
    id:int # 100
    name:str # '格里芬'
    character_des:str # '单位来自格里芬'

class UnitCharacter(ConfigTable):
    name = 'unit_character'

    def add_instance(self,k):
        return UnitCharacterInstance(**self._data[k])    
