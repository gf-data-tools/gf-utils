
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class EquipInAllyInfoInstance:
    id:str # '1'
    equip_id:str # '37'
    equip_level:str # '0'
    pow:str # '0'
    hit:str # '0'
    dodge:str # '0'
    speed:str # '0'
    rate:str # '0'
    critical_harm_rate:str # '0'
    critical_percent:str # '0'
    armor_piercing:str # '0'
    armor:str # '0'
    shield:str # '0'
    damage_amplify:str # '0'
    damage_reduction:str # '0'
    night_view_percent:str # '0'
    bullet_number_up:str # '0'

class EquipInAllyInfo(ConfigTable):
    name = 'equip_in_ally_info'

    def add_instance(self,k):
        return EquipInAllyInfoInstance(**self._data[k])    
