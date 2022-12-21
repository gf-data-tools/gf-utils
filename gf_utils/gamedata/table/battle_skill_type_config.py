
from ._base import ConfigTable
from dataclasses import dataclass

@dataclass
class BattleSkillTypeConfigInstance:
    id:int # 101
    charge_time:int # 360
    charge_tier:int # 3
    start_charge_tier:int # 1

class BattleSkillTypeConfig(ConfigTable):
    name = 'battle_skill_type_config'

    def add_instance(self,k):
        return BattleSkillTypeConfigInstance(**self._data[k])    
