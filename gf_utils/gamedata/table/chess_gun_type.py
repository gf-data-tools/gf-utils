
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class ChessGunTypeInstance:
    id:int # 1
    name:str # '手枪'
    power:int # 4
    range:int # 2
    hp:int # 10
    ap:int # 2
    attack_times:int # 1
    armor:int # 0
    armor_piercing:int # 0
    gun_type_skill:str # '201'
    attack_angle:int # 2
    passive_skill:str # ''
    ai_passive_skill:str # ''

class ChessGunType(ConfigTable):
    name = 'chess_gun_type'

    def add_instance(self,k):
        return ChessGunTypeInstance(**self._data[k])    
