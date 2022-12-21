
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadChipInstance:
    id:int # 2011
    name:str # '*2星1格'
    rank:int # 2
    color:str # '1,2'
    grid:str # '1'
    is_random:int # 1
    random_number:str # '1,1'
    assist_damage:int # 85
    assist_def_break:int # 51
    assist_hit:int # 35
    assist_reload:int # 22
    intensity_ratio:int # 28
    grid_number:int # 1
    damage:int # 0
    atk_speed:int # 0
    hit:int # 0
    def:int # 0
    bonus_type:str # ''
    type:int # 1
    fit_squads:str # ''
    develop_duration:int # 28800

class SquadChip(ConfigTable):
    name = 'squad_chip'

    def add_instance(self,k):
        return SquadChipInstance(**self._data[k])    
