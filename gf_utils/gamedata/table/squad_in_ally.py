
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class SquadInAllyInstance:
    id:int # 1
    squad_id:int # 1
    squad_level:int # 90
    cpu_level:int # 50
    squad_completion_level:int # 1
    rank:int # 1
    advanced_level:int # 1
    assist_damage:int # 0
    assist_reload:int # 0
    assist_hit:int # 0
    assist_def_break:int # 0
    damage:int # 0
    atk_speed:int # 0
    hit:int # 0
    def:int # 0
    skill1:int # 10
    skill2:int # 10
    skill3:int # 10
    skin:int # 0

class SquadInAlly(ConfigTable):
    name = 'squad_in_ally'

    def add_instance(self,k):
        return SquadInAllyInstance(**self._data[k])    
