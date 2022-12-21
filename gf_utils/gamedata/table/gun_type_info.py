
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class GunTypeInfoInstance:
    id:str # '1'
    name:str # '手枪'
    basic_attribute_life:str # '0.60'
    basic_attribute_pow:str # '0.60'
    basic_attribute_rate:str # '0.80'
    basic_attribute_speed:str # '1.50'
    basic_attribute_hit:str # '1.20'
    basic_attribute_dodge:str # '1.80'
    basic_attribute_armor:str # '0.00'
    mp_fix_ratio:str # '2.00'
    part_fix_ratio:str # '0.70'
    fix_time_ratio:str # '0.50'

class GunTypeInfo(ConfigTable):
    name = 'gun_type_info'

    def add_instance(self,k):
        return GunTypeInfoInstance(**self._data[k])    
